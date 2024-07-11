from typing import List, Optional, Union
from datetime import date

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

    def __repr__(self):
        return f"Patient({self.patient_id}, {self.sexe}, {self.age_baseline})"
