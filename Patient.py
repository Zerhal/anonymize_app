from typing import List, Optional, Union
from datetime import date
import random
            

class Patient:
    def __init__(self, 
                 patient_id: str,
                 sexe: str,
                 mutations: int,
                 genes: List[str],
                 pathogenicite: List[int],
                 statut_variant: List[str],
                 mort_subite_antcd: str,
                 age_dg_cmh: float,
                 hospit_non_programmee: str,
                 fibrillation_ventriculaire: str,
                 tachycardie_ventriculaire: str,
                 fibrillation_auriculaire: str,
                 flutter_auriculaire: str,
                 avc_ait: str,
                 mort_subite_recuperee: str,
                 pose_pm: str,
                 pose_dai: str,
                 type_prevention_dai: Optional[str],
                 choc_approprie: str,
                 alcoolisation_coronaire: str,
                 myomectomie: str,
                 syncope: str,
                 date_syncopes: Optional[date],
                 date_baseline: date,
                 age_baseline: float,
                 bmi: float,
                 bsa: float,
                 dyspnee_nyha: str,
                 epaisseur_paroi_vg: float,
                 fraction_ejection_vg: float,
                 diametre_oreillette_gauche: float,
                 volume_oreillette_gauche: float,
                 gradient_intravg_repos: float,
                 gradient_intravg_vasalva: float,
                 tvns_holter: str,
                 tvns_effort: str,
                 valeur_bnp: float,
                 valeur_nt_pro_bnp: Union[float, str],
                 irm_rehaussement_tardif_t1: float,
                 quantite_masse_vg: float,
                 pas_effort_maxi: float,
                 valeur_effort_maximum: float,
                 unite_effort_maximum: str,
                 qrs_120ms: str,
                 hospit_non_programmee_post_baseline: str,
                 date_1ere_hospit_ic_post_baseline: Optional[date],
                 fv_post_baseline: str,
                 date_1er_fv_post_baseline: Optional[date],
                 tvs_post_baseline: str,
                 date_1er_tvs_post_baseline: Optional[date],
                 fa_post_baseline: str,
                 date_1er_fa_post_baseline: Optional[date],
                 flutter_auriculaire_post_baseline: str,
                 date_1er_flutter_post_baseline: Optional[date],
                 avc_ait_post_baseline: str,
                 date_avc_ait_post_baseline: Optional[date],
                 msr_post_baseline: str,
                 date_1er_msr_post_baseline: Optional[date],
                 pm_post_baseline: str,
                 dai_post_baseline: str,
                 type_prevention_dai_post_baseline: Optional[str],
                 choc_approprie_post_baseline: str,
                 date_choc_post_baseline: Optional[date],
                 transplantation_cardiaque: str,
                 date_transplantation_cardiaque: Optional[date],
                 alcoolisation_coronaire_post_baseline: str,
                 date_alcoolisation_coronaire_post_baseline: Optional[date],
                 myomectomie_post_baseline: str,
                 date_myomectomie_post_baseline: Optional[date],
                 dcd: str,
                 cause_deces: Optional[str]):
        self.patient_id = patient_id
        self.sexe = sexe
        self.mutations = mutations
        self.genes = genes
        self.pathogenicite = pathogenicite
        self.statut_variant = statut_variant
        self.mort_subite_antcd = mort_subite_antcd
        self.age_dg_cmh = age_dg_cmh
        self.hospit_non_programmee = hospit_non_programmee
        self.fibrillation_ventriculaire = fibrillation_ventriculaire
        self.tachycardie_ventriculaire = tachycardie_ventriculaire
        self.fibrillation_auriculaire = fibrillation_auriculaire
        self.flutter_auriculaire = flutter_auriculaire
        self.avc_ait = avc_ait
        self.mort_subite_recuperee = mort_subite_recuperee
        self.pose_pm = pose_pm
        self.pose_dai = pose_dai
        self.type_prevention_dai = type_prevention_dai
        self.choc_approprie = choc_approprie
        self.alcoolisation_coronaire = alcoolisation_coronaire
        self.myomectomie = myomectomie
        self.syncope = syncope
        self.date_syncopes = date_syncopes
        self.date_baseline = date_baseline
        self.age_baseline = age_baseline
        self.bmi = bmi
        self.bsa = bsa
        self.dyspnee_nyha = dyspnee_nyha
        self.epaisseur_paroi_vg = epaisseur_paroi_vg
        self.fraction_ejection_vg = fraction_ejection_vg
        self.diametre_oreillette_gauche = diametre_oreillette_gauche
        self.volume_oreillette_gauche = volume_oreillette_gauche
        self.gradient_intravg_repos = gradient_intravg_repos
        self.gradient_intravg_vasalva = gradient_intravg_vasalva
        self.tvns_holter = tvns_holter
        self.tvns_effort = tvns_effort
        self.valeur_bnp = valeur_bnp
        self.valeur_nt_pro_bnp = valeur_nt_pro_bnp
        self.irm_rehaussement_tardif_t1 = irm_rehaussement_tardif_t1
        self.quantite_masse_vg = quantite_masse_vg
        self.pas_effort_maxi = pas_effort_maxi
        self.valeur_effort_maximum = valeur_effort_maximum
        self.unite_effort_maximum = unite_effort_maximum
        self.qrs_120ms = qrs_120ms
        self.hospit_non_programmee_post_baseline = hospit_non_programmee_post_baseline
        self.date_1ere_hospit_ic_post_baseline = date_1ere_hospit_ic_post_baseline
        self.fv_post_baseline = fv_post_baseline
        self.date_1er_fv_post_baseline = date_1er_fv_post_baseline
        self.tvs_post_baseline = tvs_post_baseline
        self.date_1er_tvs_post_baseline = date_1er_tvs_post_baseline
        self.fa_post_baseline = fa_post_baseline
        self.date_1er_fa_post_baseline = date_1er_fa_post_baseline
        self.flutter_auriculaire_post_baseline = flutter_auriculaire_post_baseline
        self.date_1er_flutter_post_baseline = date_1er_flutter_post_baseline
        self.avc_ait_post_baseline = avc_ait_post_baseline
        self.date_avc_ait_post_baseline = date_avc_ait_post_baseline
        self.msr_post_baseline = msr_post_baseline
        self.date_1er_msr_post_baseline = date_1er_msr_post_baseline
        self.pm_post_baseline = pm_post_baseline
        self.dai_post_baseline = dai_post_baseline
        self.type_prevention_dai_post_baseline = type_prevention_dai_post_baseline
        self.choc_approprie_post_baseline = choc_approprie_post_baseline
        self.date_choc_post_baseline = date_choc_post_baseline
        self.transplantation_cardiaque = transplantation_cardiaque
        self.date_transplantation_cardiaque = date_transplantation_cardiaque
        self.alcoolisation_coronaire_post_baseline = alcoolisation_coronaire_post_baseline
        self.date_alcoolisation_coronaire_post_baseline = date_alcoolisation_coronaire_post_baseline
        self.myomectomie_post_baseline = myomectomie_post_baseline
        self.date_myomectomie_post_baseline = date_myomectomie_post_baseline
        self.dcd = dcd
        self.cause_deces = cause_deces


    

    def anonymize(self):
        def top_bottom_coding(value, lower_bound, upper_bound):
            """
            Apply top/bottom coding to a value, ensuring it falls within the specified bounds.
            
            Parameters:
            - value: The value to be coded. It can be of any type that supports comparison.
            - lower_bound: The lower bound for the value.
            - upper_bound: The upper bound for the value.
            
            Returns:
            - The value after applying top/bottom coding.
            """

            if value is None:
                return value
            try:
                if isinstance(value, str):
                    # Attempt to convert to float if value is a string
                    value = float(value.replace(',', '.'))  # handle comma as decimal separator
                
                # Ensure lower_bound and upper_bound are comparable to value
                lower_bound = float(lower_bound)
                upper_bound = float(upper_bound)
                
                # Apply top/bottom coding
                coded_value = max(lower_bound, min(value, upper_bound))
                return coded_value
            except (ValueError, TypeError) as e:
                # Handle cases where conversion to float or comparison fails
                print(f"Error in top_bottom_coding: {e}")
                return None
        
        def rank_swapping(value):
            if value is None:
                return value
            if(isinstance(value, float)):
                value = int(value)
            value += 1
            return value
        
        def post_randomisation(value, noise_level=0.05):
            """
            Apply post-randomisation by adding small random noise to a value.
            
            Parameters:
            - value: The value to be anonymized. Expected to be a numeric type (int or float).
            - noise_level: The maximum percentage of noise to add or subtract from the value (0 to 1).
            
            Returns:
            - The anonymized value after adding random noise.
            """

            if value is None:
                return value
            try:
                # Ensure value is a float
                value = float(value)
                
                # Ensure noise_level is between 0 and 1
                if not 0 <= noise_level <= 1:
                    raise ValueError("Noise level must be between 0 and 1")
                
                # Calculate the noise as a percentage of the value
                noise = value * random.uniform(-noise_level, noise_level)
                anonymized_value = value + noise
                
                return anonymized_value
            except (ValueError, TypeError) as e:
                # Handle cases where the value cannot be converted to float or is not numeric
                print(f"Error in post_randomisation: {e}")
                return value
        
        def t_closeness(value):
            return value

        # Dictionary of attribute names to their anonymization techniques
        anonymization_techniques = {
            'age_dg_cmh': ('top_bottom_coding', 0, 100),
            'date_syncopes': 't_closeness',
            'date_baseline': 't_closeness',
            'age_baseline': ('top_bottom_coding', 0, 100),
            'bmi': 'rank_swapping',
            'bsa': ('post_randomisation', 0.05),
            'epaisseur_paroi_vg': ('top_bottom_coding', 5, 25),
            'fraction_ejection_vg': ('post_randomisation', 0.05),
            'diametre_oreillette_gauche': ('top_bottom_coding', 10, 50),
            'volume_oreillette_gauche': ('post_randomisation', 0.05),
            'gradient_intravg_repos': ('post_randomisation', 0.05),
            'gradient_intravg_vasalva': ('post_randomisation', 0.05),
            'valeur_nt_pro_bnp': ('top_bottom_coding', 0, 10000),
            'date_1ere_hospit_ic_post_baseline': 't_closeness',
            'date_1er_fv_post_baseline': 't_closeness',
            'date_1er_tvs_post_baseline': 't_closeness',
            'date_1er_fa_post_baseline': 't_closeness',
            'date_1er_flutter_post_baseline': 't_closeness',
            'date_avc_ait_post_baseline': 't_closeness'
        }
        
        anonymized_data = {}
        for attr, technique in anonymization_techniques.items():
            if isinstance(technique, str):
                method = locals()[technique]
                anonymized_data[attr] = method(getattr(self, attr))
            elif isinstance(technique, tuple):
                method_name, *params = technique
                method = locals()[method_name]
                anonymized_data[attr] = method(getattr(self, attr), *params)

        return anonymized_data

    def __repr__(self):
        return f"Patient({self.patient_id}, {self.sexe}, {self.age_baseline})"
    