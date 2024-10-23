variables = {
    'mecanismes_filtre' : 'p1',
    'procesos_marcados_1': 'a1a_1',
    'suma_organos_1': ['a1.1a', 'a1.1b', 'a1.1c', 'a1.1d', 'a1.1e', 'a1.1f'],
    'procesos_marcados_2': 'a1b_1',
    'suma_procesos_2': ['a2.1a', 'a2.1b', 'a2.1c'],
    'total_procesos_2': 'a2.1d',
    'total_procesos_planes': 'a2.1a',
    'procesos_marcados_a_planes': [
        'a2.1.1_1', 'a2.1.1_2', 'a2.1.1_3', 'a2.1.1_4', 'a2.1.1_5', 
        'a2.1.1_6', 'a2.1.1_7', 'a2.1.1_8', 'a2.1.1_9', 'a2.1.1_10', 
        'a2.1.1_11', 'a2.1.1_12', 'a2.1.1_13', 'a2.1.1_14', 'a2.1.1_15', 
        'a2.1.1_16', 'a2.1.1_17', 'a2.1.1_18', 'a2.1.1_19', 'a2.1.1_20', 
        'a2.1.1_21', 'a2.1.1_22', 'a2.1.1_23', 'a2.1.1_24', 'a2.1.1_25', 
        'a2.1.1_26', 'A2.1.2'
    ],
    'pacto_bool' : 'a1c_1',
    'num_pactos' : 'a3.1',
    'audiencias_bool': 'a1d_1',
    'num_audiencias_2023': 'a4.1a',
    'num_audiencias_2024': 'a4.1b',
    'consultes_bool': 'a1e_1',
    'total_consultes': 'a5.1',
    'referendums_bool': 'a1g_1',
    'total_referendums': 'a7.1',
    'iniciatives_bool': 'a1f_1',
    'total_iniciatives': 'a6.1',
    'intervencions_bool': 'a1h_1',
    'total_intervencions': 'a8.1',
    'altres_bool': 'a1i_1',
    'total_altres': 'a9.1a',
    'mec_digital' : 'p3',
    'plataforma_dig_no': 'd1_4',
    'sistema_gest_dig' : 'd4',
    'dades_obertes_no': 'd5_3',
    'suport_entitats' : 'p4',
    'no_suport_unio_europea': 'e1.1a_5',
    'no_suport_govern_central': 'e1.1b_5',
    'no_suport_generalitat': 'e1.1c_5',
    'no_suport_diputacio': 'e1.1d_5',
    'no_suport_consell_comarcal': 'e1.1e_5',
    'no_suport_consorci': 'e1.1f_5',
    'no_suport_mancomunitat': 'e1.1g_5',
    'no_suport_altres_entitats': 'e1.1h_5'
}

variable_siempre_presente = ['q9','q6', 'q7']

reglas = {
    'mecanismes_si_despres_no':{
        'condicion': f"(df[variables['mecanismes_filtre']] == 1) & " \
                 f"(df[[variables['procesos_marcados_1'], variables['procesos_marcados_2'], variables['pacto_bool'], " \
                 f"variables['audiencias_bool'], variables['consultes_bool'], variables['iniciatives_bool'], " \
                 f"variables['referendums_bool'], variables['intervencions_bool'], variables['altres_bool']]].fillna(0).sum(axis=1) <= 0)",
        'mensaje': "Ha marcat mecanismes i despres tot 0 o NA",
        'variables': [
            variables['mecanismes_filtre'], variables['procesos_marcados_1'], variables['procesos_marcados_2'],
            variables['pacto_bool'], variables['audiencias_bool'], variables['consultes_bool'], variables['iniciatives_bool'], 
            variables['referendums_bool'], variables['intervencions_bool'], variables['altres_bool']
        ]
    },
    'organs_suma_zero': {
        'condicion': f"(pd.notna(df[variables['procesos_marcados_1']])) & (df[variables['procesos_marcados_1']] == 1) & (df[variables['suma_organos_1']].sum(axis=1) <= 0)",
        'mensaje': "Ha marcat òrgans però la suma és = 0",
        'variables': [variables['procesos_marcados_1']] + variables['suma_organos_1']
    },
    'processos_suma_zero': {
        'condicion': f"(pd.notna(df[variables['procesos_marcados_2']])) & (df[variables['procesos_marcados_2']] == 1) & (df[variables['suma_procesos_2']].sum(axis=1) <= 0)",
        'mensaje': "Ha marcat processos però la suma és = 0",
        'variables': [variables['procesos_marcados_2']] + variables['suma_procesos_2']
    },
    'pactes_na': {
        'condicion': f"(pd.notna(df[variables['pacto_bool']])) & (df[variables['pacto_bool']] == 1) & (pd.isna(df[variables['num_pactos']]))",
        'mensaje': "Ha marcat que ha realitzat pactes però no ha especificat cap pacte (NA).",
        'variables': [variables['pacto_bool'], variables['num_pactos']]
    },
    'audiencies_suma_zero': {
        'condicion': f"(pd.notna(df[variables['audiencias_bool']])) & " \
                    f"(df[variables['audiencias_bool']] == 1) & " \
                    f"(df[variables['num_audiencias_2023']].fillna(0) == 0) & " \
                    f"(df[variables['num_audiencias_2024']].fillna(0) == 0)",
        'mensaje': "Ha marcat que ha realitzat audiències però no posa cap nombre d'audiències vàlid per al 2023 o 2024.",
        'variables': [variables['audiencias_bool'], variables['num_audiencias_2023'], variables['num_audiencias_2024']]
    },
    'consultes_suma_zero': {
        'condicion': f"(pd.notna(df[variables['consultes_bool']])) & (df[variables['consultes_bool']] == 1) & (pd.to_numeric(df[variables['total_consultes']], errors='coerce').fillna(0) <= 0)",
        'mensaje': "Ha marcat que ha realitzat consultes però no posa un nombre de consultes vàlid.",
        'variables': [variables['consultes_bool'], variables['total_consultes']]
    },
    'referendums_suma_zero': {
        'condicion': f"(pd.notna(df[variables['referendums_bool']])) & (df[variables['referendums_bool']] == 1) & (pd.to_numeric(df[variables['total_referendums']], errors='coerce').fillna(0).sum() <= 0)",
        'mensaje': "Ha marcat que ha realitzat referèndums però no posa un nombre de referèndums vàlid.",
        'variables': [variables['referendums_bool'], variables['total_referendums']]
    },
    'iniciatives_suma_zero': {
        'condicion': f"(df[variables['iniciatives_bool']] == 1) & (df[variables['total_iniciatives']].apply(pd.to_numeric, errors='coerce').fillna(0).sum() == 0)",
        'mensaje': "Ha marcat que ha realitzat iniciatives però la suma total és igual a 0.",
        'variables': [variables['iniciatives_bool'], variables['total_iniciatives']]
    },
    'intervencions_suma_zero': {
        'condicion': f"(df[variables['intervencions_bool']] == 1) & " \
                    f"(pd.to_numeric(df[variables['total_intervencions']], errors='coerce').fillna(1) == 0)",
        'mensaje': "Ha marcat que ha realitzat intervencions però la suma total és 0.",
        'variables': [variables['intervencions_bool'], variables['total_intervencions']]
    },
    'mecanismes_digitals_invalids': {
        'condicion': f"(df[variables['mec_digital']] == 1) & (df[variables['plataforma_dig_no']] == 1) & (df[variables['sistema_gest_dig']] == 2) & (df[variables['dades_obertes_no']] == 1)",
        'mensaje': "Posa que disposa de mecanismes digitals però no marca cap opció vàlida (Revisar D1, D4 i D5)",
        'variables': [variables['mec_digital'], variables['plataforma_dig_no'], variables['sistema_gest_dig'], variables['dades_obertes_no']]
    },
    'suport_entitats_tot_no': {
        'condicion': f"(df[variables['suport_entitats']] == 1) & " \
                     f"(df[[variables['no_suport_unio_europea'], variables['no_suport_govern_central'], " \
                     f"variables['no_suport_generalitat'], variables['no_suport_diputacio'], " \
                     f"variables['no_suport_consell_comarcal'], variables['no_suport_consorci'], " \
                     f"variables['no_suport_mancomunitat'], variables['no_suport_altres_entitats']]].sum(axis=1) == 8)",
        'mensaje': "Ha marcat que té suport d'entitats però no ha indicat cap suport vàlid (totes les opcions marcades com a 'Cap suport').",
        'variables': [
            variables['suport_entitats'], variables['no_suport_unio_europea'], variables['no_suport_govern_central'], 
            variables['no_suport_generalitat'], variables['no_suport_diputacio'], variables['no_suport_consell_comarcal'], 
            variables['no_suport_consorci'], variables['no_suport_mancomunitat'], variables['no_suport_altres_entitats']
        ]
    }


}