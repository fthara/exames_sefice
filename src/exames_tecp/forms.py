from django import forms

from .models import Exame_TECP, Pdf_TECP
from pacientes.models import Paciente

class PdfForm(forms.ModelForm):
    pdf = forms.FileField()
    class Meta:
        model = Exame_TECP
        exclude = ()
        fields = [
            'pdf',
        ]

class ExameTecpForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(queryset = Paciente.objects.all(), label = 'Nome')
    data_exame = forms.DateField(label = 'Data')
    peso = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Peso')
    altura = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Altura')
    IMC = forms.DecimalField(max_digits=5, decimal_places=2, label = 'IMC')

    Delta_VO2_W = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Delta VO2/W')
    Delta_VE_VCO2 = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Delta VE/VCO2MC')
    Delta_FC_VO2 = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Delta FC/VO2')
    VE_VVM= forms.DecimalField(max_digits=5, decimal_places=2, label = 'VE/VVM')
    SpO2 = forms.DecimalField(max_digits=5, decimal_places=2, label = 'SpO2')
    Borg = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Borg')

    Time_Rest = forms.TimeField(label = 'Time (min) - Rest')
    Time_AT = forms.TimeField(label = 'Time (min) - AT')
    Time_VO2Max = forms.TimeField(label = 'Time (min) - VO2 Max')
    Work_Rest = forms.IntegerField(label = 'Work (Wats) - Rest')
    Work_AT = forms.IntegerField(label = 'Work (Wats) - AT')
    Work_VO2Max = forms.IntegerField(label = 'Work (Wats) - VO2 Max')
    Work_Pred = forms.IntegerField(label = 'Work (Wats) - Pred')
    Work_VO2MaxPred = forms.IntegerField(label = 'Work (Wats) - VO2 Max/Pred (%)')
    Ex_Time_AT = forms.TimeField(label = 'Ex Time (min) - AT')
    Ex_Time_VO2Max = forms.TimeField(label = 'Ex Time (min) - VO2 Max')

    VO2_Rest_ml_min = forms.IntegerField(label = 'VO2 (mL/min) - Rest')
    VO2_AT_ml_min = forms.IntegerField(label = 'VO2 (mL/min) - AT')
    VO2_VO2Max_ml_min = forms.IntegerField(label = 'VO2 (mL/min) - VO2 Max')
    VO2_Pred_ml_min = forms.IntegerField(label = 'VO2 (mL/min) - Pred')
    VO2_VO2MaxPred_ml_min = forms.IntegerField(label = 'VO2 (mL/min) - VO2 Max/Pred (%)')
    VO2_Rest_ml_kg_min = forms.DecimalField(max_digits=5, decimal_places=2, label = 'VO2 (mL/kg/min) - Rest')
    VO2_AT_ml_kg_min = forms.DecimalField(max_digits=5, decimal_places=2, label = 'VO2 (mL/kg/min) - AT')
    VO2_VO2Max_ml_kg_min = forms.DecimalField(max_digits=5, decimal_places=2, label = 'VO2 (mL/kg/min) - VO2 Max')
    VO2_Pred_ml_kg_min = forms.DecimalField(max_digits=5, decimal_places=2, label = 'VO2 (mL/kg/min) - Pred')
    VO2_VO2MaxPred_ml_kg_min = forms.IntegerField(label = 'VO2 (mL/kg/min) - VO2 Max/Pred (%)')
    VCO2_Rest = forms.IntegerField(label = 'VCO2 (mL/min) - VO2 Max/Pred (%)')
    VCO2_AT = forms.IntegerField(label = 'VCO2 (mL/min) - AT')
    VCO2_VO2Max = forms.IntegerField(label = 'VCO2 (mL/min) - VO2 Max')
    VCO2_Pred = forms.IntegerField(label = 'VCO2 (mL/min) - Pred')
    VCO2_VO2MaxPred = forms.IntegerField(label = 'VCO2 (mL/min) - VO2 Max/Pred (%)')
    RER_Rest = forms.DecimalField(max_digits=5, decimal_places=2, label = 'RER - Rest')
    RER_AT = forms.DecimalField(max_digits=5, decimal_places=2, label = 'RER - AT')
    RER_VO2Max = forms.DecimalField(max_digits=5, decimal_places=2, label = 'RER - VO2 Max')

    VE_BTPS_Rest = forms.DecimalField(max_digits=5, decimal_places=2, label = 'VE BTPS (L/min) - Rest')
    VE_BTPS_AT = forms.DecimalField(max_digits=5, decimal_places=2, label = 'VE BTPS (L/min) - AT')
    VE_BTPS_VO2Max = forms.DecimalField(max_digits=5, decimal_places=2, label = 'VE BTPS (L/min) - VO2 Max')
    VE_BTPS_Pred = forms.DecimalField(max_digits=5, decimal_places=2, label = 'VE BTPS (L/min) - Pred')
    VE_BTPS_VO2MaxPred = forms.IntegerField(label = 'VE BTPS (L/min) - VO2 Max/Pred (%)')
    Vt_BTPS_Rest = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Vt BTPS (L) - Rest')
    Vt_BTPS_AT = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Vt BTPS (L) - AT')
    Vt_BTPS_VO2Max = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Vt BTPS (L) - VO2 Max')
    RR_Rest = forms.IntegerField(label = 'RR (br/min) - Rest')
    RR_AT = forms.IntegerField(label = 'RR (br/min) - AT')
    RR_VO2Max = forms.IntegerField(label = 'RR (br/min) - VO2 Max')
    VE_VO2_Rest = forms.IntegerField(label = 'VE/VO2 - Rest')
    VE_VO2_AT = forms.IntegerField(label = 'VE/VO2 - AT')
    VE_VO2_VO2Max = forms.IntegerField(label = 'VE/VO2 - VO2 Max')
    VE_VO2_Pred = forms.IntegerField(label = 'VE/VO2 - Pred')
    VE_VO2_VO2MaxPred = forms.IntegerField(label = 'VE/VO2 - VO2 Max/Pred (%)')
    VE_VCO2_Rest = forms.IntegerField(label = 'VE/VCO2 - Pred')
    VE_VCO2_AT = forms.IntegerField(label = 'VE/VCO2 - AT')
    VE_VCO2_VO2Max = forms.IntegerField(label = 'VE/VCO2 - VO2 Max')
    VE_VCO2_Pred = forms.IntegerField(label = 'VE/VCO2 - Pred')
    VE_VCO2_VO2MaxPred = forms.IntegerField(label = 'VE/VCO2 - VO2 Max/Pred (%)')
    Ti_Ttot_Rest = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Ti/Ttot - Rest')
    Ti_Ttot_AT = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Ti/Ttot - AT')
    Ti_Ttot_VO2Max = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Ti/Ttot - VO2 Max')
    Ti_Rest = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Ti - Rest')
    Ti_AT = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Ti - AT')
    Ti_VO2Max = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Ti - VO2 Max')
    Te_Rest = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Te - Rest')
    Te_AT = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Te - AT')
    Te_VO2Max = forms.DecimalField(max_digits=5, decimal_places=2, label = 'Te - VO2 Max')

    HeartRate_Rest = forms.IntegerField(label = 'HeartRate (BPM) - Rest')
    HeartRate_AT = forms.IntegerField(label = 'HeartRate (BPM) - AT')
    HeartRate_VO2Max = forms.IntegerField(label = 'HeartRate (BPM) - VO2 Max')
    HeartRate_Pred = forms.IntegerField(label = 'HeartRate (BPM) - Pred')
    HeartRate_VO2MaxPred = forms.IntegerField(label = 'HeartRate (BPM) - VO2 Max/Pred (%)')    
    VO2_HR_Rest = forms.IntegerField(label = 'VO2/HR (mL/beat) - Rest')
    VO2_HR_AT = forms.IntegerField(label = 'VO2/HR (mL/beat) - AT')
    VO2_HR_VO2Max = forms.IntegerField(label = 'VO2/HR (mL/beat) - VO2 Max')
    VO2_HR_Pred = forms.IntegerField(label = 'VO2/HR (mL/beat) - Pred')
    VO2_HR_VO2MaxPred = forms.IntegerField(label = 'VO2/HR (mL/beat) - VO2 Max/Pred (%)')
    
    PETO2_Rest = forms.IntegerField(label = 'PETO2 (mmHg) - Rest')
    PETO2_AT = forms.IntegerField(label = 'PETO2 (mmHg) - AT')
    PETO2_VO2Max = forms.IntegerField(label = 'PETO2 (mmHg) - VO2 Max')
    PETCO2_Rest = forms.IntegerField(label = 'PETCO2 (mmHg) - Rest')
    PETCO2_AT = forms.IntegerField(label = 'PETCO2 (mmHg) - AT')
    PETCO2_VO2Max = forms.IntegerField(label = 'PETCO2 (mmHg) - VO2 Max')
    
    class Meta:
        model = Exame_TECP
        exclude = ()
        fields = [
            'paciente',
            'data_exame',
            'peso',
            'altura',
            'IMC',
            'Delta_VO2_W',
            'Delta_VE_VCO2',
            'Delta_FC_VO2',
            'VE_VVM',
            'SpO2',
            'Borg',
            'Time_Rest',
            'Time_AT',
            'Time_VO2Max',
            'Work_Rest',
            'Work_AT',
            'Work_VO2Max',
            'Work_Pred',
            'Work_VO2MaxPred',
            'Ex_Time_AT',
            'Ex_Time_VO2Max',
            'VO2_Rest_ml_min',
            'VO2_AT_ml_min',
            'VO2_VO2Max_ml_min',
            'VO2_Pred_ml_min',
            'VO2_VO2MaxPred_ml_min',
            'VO2_Rest_ml_kg_min',
            'VO2_AT_ml_kg_min',
            'VO2_VO2Max_ml_kg_min',
            'VO2_Pred_ml_kg_min',
            'VO2_VO2MaxPred_ml_kg_min',
            'VCO2_Rest',
            'VCO2_AT',
            'VCO2_VO2Max',
            'VCO2_Pred',
            'VCO2_VO2MaxPred',
            'RER_Rest',
            'RER_AT',
            'RER_VO2Max',
            'VE_BTPS_Rest',
            'VE_BTPS_AT',
            'VE_BTPS_VO2Max',
            'VE_BTPS_Pred',
            'VE_BTPS_VO2MaxPred',
            'Vt_BTPS_Rest',
            'Vt_BTPS_AT',
            'Vt_BTPS_VO2Max',
            'RR_Rest',
            'RR_AT',
            'RR_VO2Max',
            'VE_VO2_Rest',
            'VE_VO2_AT',
            'VE_VO2_VO2Max',
            'VE_VO2_Pred',
            'VE_VO2_VO2MaxPred',
            'VE_VCO2_Rest',
            'VE_VCO2_AT',
            'VE_VCO2_VO2Max',
            'VE_VCO2_Pred',
            'VE_VCO2_VO2MaxPred',
            'Ti_Ttot_Rest',
            'Ti_Ttot_AT',
            'Ti_Ttot_VO2Max',
            'Ti_Rest',
            'Ti_AT',
            'Ti_VO2Max',
            'Te_Rest',
            'Te_AT',
            'Te_VO2Max',
            'HeartRate_Rest',
            'HeartRate_AT',
            'HeartRate_VO2Max',
            'HeartRate_Pred',
            'HeartRate_VO2MaxPred',
            'VO2_HR_Rest',
            'VO2_HR_AT',
            'VO2_HR_VO2Max',
            'VO2_HR_Pred',
            'VO2_HR_VO2MaxPred',
            'PETO2_Rest',
            'PETO2_AT',
            'PETO2_VO2Max',
            'PETCO2_Rest',
            'PETCO2_AT',
            'PETCO2_VO2Max',
        ]