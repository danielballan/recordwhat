from ophyd import (Device, EpicsSignal, EpicsSignalRO,
                   Component as Cpt)
from .record_info import load_info_file


class RecordBase(Device):
    alarm_acknowledge_severity = Cpt(EpicsSignalRO, '.ACKS')
    alarm_acknowledge_transient = Cpt(EpicsSignalRO, '.ACKT')
    access_security_group = Cpt(EpicsSignal, '.ASG')
    description = Cpt(EpicsSignal, '.DESC')
    scan_disable_input_link_value = Cpt(EpicsSignal, '.DISA')
    disable_putfields = Cpt(EpicsSignal, '.DISP')
    disable_alarm_severity = Cpt(EpicsSignal, '.DISS')
    disable_value = Cpt(EpicsSignal, '.DISV')
    device_type = Cpt(EpicsSignal, '.DTYP')
    event_number = Cpt(EpicsSignal, '.EVNT')
    forward_link = Cpt(EpicsSignal, '.FLNK')
    lock_count = Cpt(EpicsSignalRO, '.LCNT')
    record_name = Cpt(EpicsSignalRO, '.NAME')
    new_alarm_severity = Cpt(EpicsSignalRO, '.NSEV')
    new_alarm_status = Cpt(EpicsSignalRO, '.NSTA')
    processing_active = Cpt(EpicsSignalRO, '.PACT')
    scan_phase_number = Cpt(EpicsSignal, '.PHAS')
    process_at_initialization = Cpt(EpicsSignal, '.PINI')
    priority = Cpt(EpicsSignal, '.PRIO')
    process_record = Cpt(EpicsSignal, '.PROC')
    dbputfield_process = Cpt(EpicsSignalRO, '.PUTF')
    reprocess = Cpt(EpicsSignalRO, '.RPRO')
    scanning_rate = Cpt(EpicsSignal, '.SCAN')
    scan_disable_input_link = Cpt(EpicsSignal, '.SDIS')
    current_alarm_severity = Cpt(EpicsSignalRO, '.SEVR')
    trace_processing = Cpt(EpicsSignal, '.TPRO')
    time_stamp_event = Cpt(EpicsSignal, '.TSE')
    time_stamp_event_link = Cpt(EpicsSignal, '.TSEL')
    val_undefined = Cpt(EpicsSignal, '.UDF')
    value = Cpt(EpicsSignal, '.VAL')

    @classmethod
    def field_metadata(cls):
        if not hasattr(cls, '_rtyp'):
            raise ValueError('No associated record type')

        rtyp = cls._rtyp

        field_to_md = load_info_file(rtyp)
        for attr, cpt in cls._sig_attrs.items():
            suffix = cpt.suffix.lstrip('.')
            if suffix in field_to_md:
                yield attr, field_to_md[suffix]
