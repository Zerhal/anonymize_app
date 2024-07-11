import pandas as pd
from datetime import datetime, date
from typing import List, Optional, Union

from Patient import Patient

def parse_date(value: str) -> Optional[date]:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None

def parse_int_list(value: str) -> List[int]:
    try:
        return [int(x.strip()) for x in value.split('/') if x.strip().isdigit()]
    except Exception:
        return []

def parse_str_list(value: str) -> List[str]:
    
    try:
        return [x.strip() for x in value.split('/') if x.strip()]
    except Exception:
        return []
    
def parese_float(value: str) -> Optional[float]:
    try:
        if (type(value) is str):
            value = value.replace(",", ".")
        return float(value)
    except ValueError:
        return None

def convert_patient_row(row: pd.Series) -> Patient:
    return Patient(
        patient_id=row["N° PATIENT"],
        sexe=row["Sexe"],
        mutations=int(row["Nombre de mutations d'intérêt (=N)"]),
        genes=parse_str_list(row["Nom du gene x N (plusieurs genes possibles)"]),
        pathogenicite=parse_int_list(row["Pathogénicité (classe du variant ) x N (plusieurs genes possibles)"]),
        statut_variant=parse_str_list(row["Statut du variant x N (plusieurs genes possibles)"]),
        mort_subite_antcd=row["Antécédents de Mort  Subite chez un ou plusieurs apparentés au premier degré de moins de 40 ans ou de MS chez un apparenté au premier degré avec HCM confirmée à tout âge (diagnostic post ou ante mortem)"],
        age_dg_cmh=parese_float(row["Âge au dg CMH"]),
        hospit_non_programmee=row["Insuffisance cardiaque nécessitant une hospitalisation non programmée "],
        fibrillation_ventriculaire=row["Fibrillation Ventriculaire (FV)"],
        tachycardie_ventriculaire=row["Tachycardie Ventriculaire soutenue (TVs)"],
        fibrillation_auriculaire=row["Fibrillation Auriculaire (FA)"],
        flutter_auriculaire=row["Flutter Auriculaire"],
        avc_ait=row["AVC & AIT "],
        mort_subite_recuperee=row["Mort Subite Récupérée "],
        pose_pm=row["Pose PM "],
        pose_dai=row["Pose DAI  "],
        type_prevention_dai=row["Si DAI,Type de prévention"] if pd.notnull(row["Si DAI,Type de prévention"]) else None,
        choc_approprie=row["Choc approprié (ou stimulation approprié) "],
        alcoolisation_coronaire=row["Alcoolisation coronaire septale "],
        myomectomie=row["Myomectomie (depuis Baseline)"],
        syncope=row["Syncope\n(Non vasovagale)"],
        date_syncopes=parse_date(row["Date des syncopes (La plus récente avant ou proche du baseline)"]),
        date_baseline=parse_date(row["Date Baseline"]),
        age_baseline=parese_float(row["Âge au Baseline (calcul auto)"]),
        bmi=parese_float(row["BMI\n(Calcul automatique)"]),
        bsa=parese_float(row["BSA\n (Calcul automatique)"]),
        dyspnee_nyha=row["Dyspnée "],
        epaisseur_paroi_vg=parese_float(row["Epaisseur max. Télédiastolique  paroi VG (2D) (mm)"]),
        fraction_ejection_vg=parese_float(row["Fraction Ejection du Ventricule Gauche (FEVG) (%)"]),
        diametre_oreillette_gauche=parese_float(row["Diamètre de l'Oreillette Gauche\n(mm)"]),
        volume_oreillette_gauche=parese_float(row["Volume Oreillette Gauche (ml/m²; en Biplan)"]),
        gradient_intravg_repos=parese_float(row["Gradient intraVG max au repos (mmHg)"]),
        gradient_intravg_vasalva=parese_float(row["Gradient intraVG max après Vasalva (mmHg)"]),
        tvns_holter=row["TVNS (triplet > 120/mn) (SUR HOLTER) "],
        tvns_effort=row["TVNS pendant l'effort (triplet > 120/mn) (SUR Eppreuve d'effort)"],
        valeur_bnp=parese_float(row["Valeur  BNP (ng/L) "]),
        valeur_nt_pro_bnp=row["Valeur  NT-pro BNP (ng/L) "] if pd.notnull(row["Valeur  NT-pro BNP (ng/L) "]) else None,
        irm_rehaussement_tardif_t1=parese_float(row["IRM Réhaussement tardif en T1"]),
        quantite_masse_vg=parese_float(row["Si RT Quantité masse VG "]),
        pas_effort_maxi=parese_float(row["PAS effort maxi(mmHg)"]),
        valeur_effort_maximum=parese_float(row["Valeur Effort maximum "]),
        unite_effort_maximum=row["Unité Effort maximum"],
        qrs_120ms=row["QRS > 120 ms"],
        hospit_non_programmee_post_baseline=row["Insuffisance cardiaque nécessitant une hospitalisation non programmée (depuis baseline)"],
        date_1ere_hospit_ic_post_baseline=parse_date(row["Date 1ère hospitalisation non programmée pour IC (depuis baseline)"]),
        fv_post_baseline=row["Fibrillation Ventriculaire (FV)\n(depuis baseline)"],
        date_1er_fv_post_baseline=parse_date(row["Date 1er evenement de Fibrillation Ventriculaire (FV)\n(depuis baseline)"]),
        tvs_post_baseline=row["Tachycardie Ventriculaire soutenue (TVs)\n(depuis baseline)"],
        date_1er_tvs_post_baseline=parse_date(row["Date 1er evenement deTachycardie Ventriculaire soutenue (TVs)\n(depuis baseline)"]),
        fa_post_baseline=row["Fibrillation Auriculaire (FA)\n(depuis baseline)"],
        date_1er_fa_post_baseline=parse_date(row["Date 1er evenement de Fibrilation Auriculaire (FA)\n(depuis baseline)"]),
        flutter_auriculaire_post_baseline=row["Flutter Auriculaire\n(depuis baseline)"],
        date_1er_flutter_post_baseline=parse_date(row["Date 1er evenement de Flutter Auriculaire\n(depuis baseline)"]),
        avc_ait_post_baseline=row["AVC & AIT (depuis baseline)"],
        date_avc_ait_post_baseline=parse_date(row["Date AVC ou AIT (depuis baseline)"]),
        msr_post_baseline=row["Mort Subite Récupérée (depuis Baseline)"],
        date_1er_msr_post_baseline=parse_date(row["Date 1er épisode de MSR (depuis Baseline)"]),
        pm_post_baseline=row["Pose PM depuis baseline "],
        dai_post_baseline=row["Pose DAI (depuis baseline) "],
        type_prevention_dai_post_baseline=row["Si DAI,Type de prévention"] if pd.notnull(row["Si DAI,Type de prévention"]) else None,
        choc_approprie_post_baseline=row["Choc approprié (ou stimulation approprié) (depuis le baseline)"],
        date_choc_post_baseline=parse_date(row["Date X n (Prendre la première date)"]),
        transplantation_cardiaque=row["Transplantation Cardiaque"],
        date_transplantation_cardiaque=parse_date(row["Date Transplantation Cardiaque"]),
        alcoolisation_coronaire_post_baseline=row["Alcoolisation coronaire septale (depuis Baseline)"],
        date_alcoolisation_coronaire_post_baseline=parse_date(row["Date Alcoolisation coronaire septale (depuis Baseline)"]),
        myomectomie_post_baseline=row["Myomectomie (depuis Baseline)"],
        date_myomectomie_post_baseline=parse_date(row["Date Myomectomie (depuis Baseline)"]),
        dcd=row["DCD décédé"],
        cause_deces=row["Cause du décès"] if pd.notnull(row["Cause du décès"]) else None
    )

def load_patients_from_csv(csv_file: str) -> List[Patient]:
    df = pd.read_csv(csv_file)
    patients = []
    for _, row in df.iterrows():
        try:
            patient = convert_patient_row(row)
            patients.append(patient)
        except Exception as e:
            print(f"Error converting row to Patient: {e}")
    return patients
