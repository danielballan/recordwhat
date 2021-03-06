from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('sub')
class SubRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    last_value_monitored = Cpt(EpicsSignalRO, '.MLST')
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
    value_of_input_a = Cpt(EpicsSignal, '.A')
    value_of_input_b = Cpt(EpicsSignal, '.B')
    value_of_input_c = Cpt(EpicsSignal, '.C')
    value_of_input_d = Cpt(EpicsSignal, '.D')
    value_of_input_e = Cpt(EpicsSignal, '.E')
    value_of_input_f = Cpt(EpicsSignal, '.F')
    value_of_input_g = Cpt(EpicsSignal, '.G')
    value_of_input_h = Cpt(EpicsSignal, '.H')
    value_of_input_i = Cpt(EpicsSignal, '.I')
    value_of_input_j = Cpt(EpicsSignal, '.J')
    value_of_input_k = Cpt(EpicsSignal, '.K')
    value_of_input_l = Cpt(EpicsSignal, '.L')

    # - alarms
    alarm_deadband = Cpt(EpicsSignal, '.HYST')
    high_alarm_limit = Cpt(EpicsSignal, '.HIGH')
    high_severity = Cpt(EpicsSignal, '.HSV')
    hihi_alarm_limit = Cpt(EpicsSignal, '.HIHI')
    hihi_severity = Cpt(EpicsSignal, '.HHSV')
    lolo_alarm_limit = Cpt(EpicsSignal, '.LOLO')
    lolo_severity = Cpt(EpicsSignal, '.LLSV')
    low_alarm_limit = Cpt(EpicsSignal, '.LOW')
    low_severity = Cpt(EpicsSignal, '.LSV')

    # - display
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    display_precision = Cpt(EpicsSignal, '.PREC')
    high_operating_rng = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')
    units_name = Cpt(EpicsSignal, '.EGU$', string=True)

    # - inputs
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

    # - sub
    bad_return_severity = Cpt(EpicsSignal, '.BRSV')
    init_routine_name = Cpt(EpicsSignalRO, '.INAM$', string=True)
    subroutine_name = Cpt(EpicsSignal, '.SNAM$', string=True)
