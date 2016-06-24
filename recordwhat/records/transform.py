from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('transform')
class TransformRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    calc_invalid = Cpt(EpicsSignal, '.CAV')
    calc_invalid_cbv = Cpt(EpicsSignal, '.CBV')
    calc_invalid_ccv = Cpt(EpicsSignal, '.CCV')
    calc_invalid_cdv = Cpt(EpicsSignal, '.CDV')
    calc_invalid_cev = Cpt(EpicsSignal, '.CEV')
    calc_invalid_cfv = Cpt(EpicsSignal, '.CFV')
    calc_invalid_cgv = Cpt(EpicsSignal, '.CGV')
    calc_invalid_chv = Cpt(EpicsSignal, '.CHV')
    calc_invalid_civ = Cpt(EpicsSignal, '.CIV')
    calc_invalid_cjv = Cpt(EpicsSignal, '.CJV')
    calc_invalid_ckv = Cpt(EpicsSignal, '.CKV')
    calc_invalid_clv = Cpt(EpicsSignal, '.CLV')
    calc_invalid_cmv = Cpt(EpicsSignal, '.CMV')
    calc_invalid_cnv = Cpt(EpicsSignal, '.CNV')
    calc_invalid_cov = Cpt(EpicsSignal, '.COV')
    calc_invalid_cpv = Cpt(EpicsSignal, '.CPV')
    code_version = Cpt(EpicsSignalRO, '.VERS')
    input_link_valid = Cpt(EpicsSignalRO, '.IAV')
    input_link_valid_ibv = Cpt(EpicsSignalRO, '.IBV')
    input_link_valid_icv = Cpt(EpicsSignalRO, '.ICV')
    input_link_valid_idv = Cpt(EpicsSignalRO, '.IDV')
    input_link_valid_iev = Cpt(EpicsSignalRO, '.IEV')
    input_link_valid_ifv = Cpt(EpicsSignalRO, '.IFV')
    input_link_valid_igv = Cpt(EpicsSignalRO, '.IGV')
    input_link_valid_ihv = Cpt(EpicsSignalRO, '.IHV')
    input_link_valid_iiv = Cpt(EpicsSignalRO, '.IIV')
    input_link_valid_ijv = Cpt(EpicsSignalRO, '.IJV')
    input_link_valid_ikv = Cpt(EpicsSignalRO, '.IKV')
    input_link_valid_ilv = Cpt(EpicsSignalRO, '.ILV')
    input_link_valid_imv = Cpt(EpicsSignalRO, '.IMV')
    input_link_valid_inv = Cpt(EpicsSignalRO, '.INV')
    input_link_valid_iov = Cpt(EpicsSignalRO, '.IOV')
    input_link_valid_ipv = Cpt(EpicsSignalRO, '.IPV')
    output_link_valid = Cpt(EpicsSignalRO, '.OAV')
    output_link_valid_obv = Cpt(EpicsSignalRO, '.OBV')
    output_link_valid_ocv = Cpt(EpicsSignalRO, '.OCV')
    output_link_valid_odv = Cpt(EpicsSignalRO, '.ODV')
    output_link_valid_oev = Cpt(EpicsSignalRO, '.OEV')
    output_link_valid_ofv = Cpt(EpicsSignalRO, '.OFV')
    output_link_valid_ogv = Cpt(EpicsSignalRO, '.OGV')
    output_link_valid_ohv = Cpt(EpicsSignalRO, '.OHV')
    output_link_valid_oiv = Cpt(EpicsSignalRO, '.OIV')
    output_link_valid_ojv = Cpt(EpicsSignalRO, '.OJV')
    output_link_valid_okv = Cpt(EpicsSignalRO, '.OKV')
    output_link_valid_olv = Cpt(EpicsSignalRO, '.OLV')
    output_link_valid_omv = Cpt(EpicsSignalRO, '.OMV')
    output_link_valid_onv = Cpt(EpicsSignalRO, '.ONV')
    output_link_valid_oov = Cpt(EpicsSignalRO, '.OOV')
    output_link_valid_opv = Cpt(EpicsSignalRO, '.OPV')
    prev_value_of_a = Cpt(EpicsSignalRO, '.LA')
    prev_value_of_b = Cpt(EpicsSignalRO, '.LB')
    prev_value_of_c = Cpt(EpicsSignalRO, '.LC')
    prev_value_of_d = Cpt(EpicsSignalRO, '.LD')
    prev_value_of_e = Cpt(EpicsSignalRO, '.LE')
    prev_value_of_f = Cpt(EpicsSignalRO, '.LF')
    prev_value_of_g = Cpt(EpicsSignalRO, '.LG')
    prev_value_of_h = Cpt(EpicsSignalRO, '.LH')
    prev_value_of_i = Cpt(EpicsSignalRO, '.LI')
    prev_value_of_j = Cpt(EpicsSignalRO, '.LJ')
    prev_value_of_k = Cpt(EpicsSignalRO, '.LK')
    prev_value_of_l = Cpt(EpicsSignalRO, '.LL')
    prev_value_of_m = Cpt(EpicsSignalRO, '.LM')
    prev_value_of_n = Cpt(EpicsSignalRO, '.LN')
    prev_value_of_o = Cpt(EpicsSignalRO, '.LO')
    prev_value_of_p = Cpt(EpicsSignalRO, '.LP')

    # - common
    calc_option = Cpt(EpicsSignal, '.COPT')
    calculation_a = Cpt(EpicsSignal, '.CLCA$', string=True)
    calculation_b = Cpt(EpicsSignal, '.CLCB$', string=True)
    calculation_c = Cpt(EpicsSignal, '.CLCC$', string=True)
    calculation_d = Cpt(EpicsSignal, '.CLCD$', string=True)
    calculation_e = Cpt(EpicsSignal, '.CLCE$', string=True)
    calculation_f = Cpt(EpicsSignal, '.CLCF$', string=True)
    calculation_g = Cpt(EpicsSignal, '.CLCG$', string=True)
    calculation_h = Cpt(EpicsSignal, '.CLCH$', string=True)
    calculation_i = Cpt(EpicsSignal, '.CLCI$', string=True)
    calculation_j = Cpt(EpicsSignal, '.CLCJ$', string=True)
    calculation_k = Cpt(EpicsSignal, '.CLCK$', string=True)
    calculation_l = Cpt(EpicsSignal, '.CLCL$', string=True)
    calculation_m = Cpt(EpicsSignal, '.CLCM$', string=True)
    calculation_n = Cpt(EpicsSignal, '.CLCN$', string=True)
    calculation_o = Cpt(EpicsSignal, '.CLCO$', string=True)
    calculation_p = Cpt(EpicsSignal, '.CLCP$', string=True)
    comment_a = Cpt(EpicsSignal, '.CMTA$', string=True)
    comment_b = Cpt(EpicsSignal, '.CMTB$', string=True)
    comment_c = Cpt(EpicsSignal, '.CMTC$', string=True)
    comment_d = Cpt(EpicsSignal, '.CMTD$', string=True)
    comment_e = Cpt(EpicsSignal, '.CMTE$', string=True)
    comment_f = Cpt(EpicsSignal, '.CMTF$', string=True)
    comment_g = Cpt(EpicsSignal, '.CMTG$', string=True)
    comment_h = Cpt(EpicsSignal, '.CMTH$', string=True)
    comment_i = Cpt(EpicsSignal, '.CMTI$', string=True)
    comment_j = Cpt(EpicsSignal, '.CMTJ$', string=True)
    comment_k = Cpt(EpicsSignal, '.CMTK$', string=True)
    comment_l = Cpt(EpicsSignal, '.CMTL$', string=True)
    comment_m = Cpt(EpicsSignal, '.CMTM$', string=True)
    comment_n = Cpt(EpicsSignal, '.CMTN$', string=True)
    comment_o = Cpt(EpicsSignal, '.CMTO$', string=True)
    comment_p = Cpt(EpicsSignal, '.CMTP$', string=True)
    display_precision = Cpt(EpicsSignal, '.PREC')
    input_a = Cpt(EpicsSignal, '.INPA$', string=True)
    input_b = Cpt(EpicsSignal, '.INPB$', string=True)
    input_c = Cpt(EpicsSignal, '.INPC$', string=True)
    input_d = Cpt(EpicsSignal, '.INPD$', string=True)
    input_e = Cpt(EpicsSignal, '.INPE$', string=True)
    input_f = Cpt(EpicsSignal, '.INPF$', string=True)
    input_g = Cpt(EpicsSignal, '.INPG$', string=True)
    input_h = Cpt(EpicsSignal, '.INPH$', string=True)
    input_i = Cpt(EpicsSignal, '.INPI$', string=True)
    input_j = Cpt(EpicsSignal, '.INPJ$', string=True)
    input_k = Cpt(EpicsSignal, '.INPK$', string=True)
    input_l = Cpt(EpicsSignal, '.INPL$', string=True)
    input_m = Cpt(EpicsSignal, '.INPM$', string=True)
    input_n = Cpt(EpicsSignal, '.INPN$', string=True)
    input_o = Cpt(EpicsSignal, '.INPO$', string=True)
    input_p = Cpt(EpicsSignal, '.INPP$', string=True)
    input_bitmap = Cpt(EpicsSignal, '.MAP')
    invalid_link_action = Cpt(EpicsSignal, '.IVLA')
    output_a = Cpt(EpicsSignal, '.OUTA$', string=True)
    output_b = Cpt(EpicsSignal, '.OUTB$', string=True)
    output_c = Cpt(EpicsSignal, '.OUTC$', string=True)
    output_d = Cpt(EpicsSignal, '.OUTD$', string=True)
    output_e = Cpt(EpicsSignal, '.OUTE$', string=True)
    output_f = Cpt(EpicsSignal, '.OUTF$', string=True)
    output_g = Cpt(EpicsSignal, '.OUTG$', string=True)
    output_h = Cpt(EpicsSignal, '.OUTH$', string=True)
    output_i = Cpt(EpicsSignal, '.OUTI$', string=True)
    output_j = Cpt(EpicsSignal, '.OUTJ$', string=True)
    output_k = Cpt(EpicsSignal, '.OUTK$', string=True)
    output_l = Cpt(EpicsSignal, '.OUTL$', string=True)
    output_m = Cpt(EpicsSignal, '.OUTM$', string=True)
    output_n = Cpt(EpicsSignal, '.OUTN$', string=True)
    output_o = Cpt(EpicsSignal, '.OUTO$', string=True)
    output_p = Cpt(EpicsSignal, '.OUTP$', string=True)
    units_name = Cpt(EpicsSignal, '.EGU$', string=True)
    value_of_a = Cpt(EpicsSignal, '.A')
    value_of_b = Cpt(EpicsSignal, '.B')
    value_of_c = Cpt(EpicsSignal, '.C')
    value_of_d = Cpt(EpicsSignal, '.D')
    value_of_e = Cpt(EpicsSignal, '.E')
    value_of_f = Cpt(EpicsSignal, '.F')
    value_of_g = Cpt(EpicsSignal, '.G')
    value_of_h = Cpt(EpicsSignal, '.H')
    value_of_i = Cpt(EpicsSignal, '.I')
    value_of_j = Cpt(EpicsSignal, '.J')
    value_of_k = Cpt(EpicsSignal, '.K')
    value_of_l = Cpt(EpicsSignal, '.L')
    value_of_m = Cpt(EpicsSignal, '.M')
    value_of_n = Cpt(EpicsSignal, '.N')
    value_of_o = Cpt(EpicsSignal, '.O')
    value_of_p = Cpt(EpicsSignal, '.P')
