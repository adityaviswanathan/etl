#!/usr/bin/env python

'''
Wrapper over models.py that enables generic constructor/query interface.
TODO(aditya): define business logic actions e.g. contract.charge_rent().
'''

__author__ = 'Aditya Viswanathan'
__email__ = 'aditya@adityaviswanathan.com'

import enum
from entities import Owner, Property, Manager, Tenant, Ticket, Unit, Contract, Contractor, ContractPayment, TicketPayment, Db


class Entity(enum.Enum):
    OWNER = 0
    PROPERTY = 1
    MANAGER = 2
    TENANT = 3
    TICKET = 4
    UNIT = 5
    CONTRACT = 6
    CONTRACTOR = 7
    CONTRACTPAYMENT = 8
    TICKETPAYMENT = 9


class ActionExecutor(object):
    @staticmethod
    def entity2string(entity_enum):
        if entity_enum is Entity.OWNER:
            return 'Owner'
        if entity_enum is Entity.PROPERTY:
            return 'Property'
        if entity_enum is Entity.MANAGER:
            return 'Manager'
        if entity_enum is Entity.TENANT:
            return 'Tenant'
        if entity_enum is Entity.TICKET:
            return 'Ticket'
        if entity_enum is Entity.UNIT:
            return 'Unit'
        if entity_enum is Entity.CONTRACT:
            return 'Contract'
        if entity_enum is Entity.CONTRACTOR:
            return 'Contractor'
        if entity_enum is Entity.CONTRACTPAYMENT:
            return 'Contractpayment'
        if entity_enum is Entity.TICKETPAYMENT:
            return 'Ticketpayment'
        raise Exception('Entity enum %s not recognized' % entity_enum)

    @staticmethod
    def string2entity(entity_str):
        entity_name = entity_str.capitalize()
        if entity_name == 'Owner':
            return Entity.OWNER
        if entity_name == 'Property':
            return Entity.PROPERTY
        if entity_name == 'Manager':
            return Entity.MANAGER
        if entity_name == 'Tenant':
            return Entity.TENANT
        if entity_name == 'Ticket':
            return Entity.TICKET
        if entity_name == 'Unit':
            return Entity.UNIT
        if entity_name == 'Contract':
            return Entity.CONTRACT
        if entity_name == 'Contractor':
            return Entity.CONTRACTOR
        if entity_name == 'Contractpayment':
            return Entity.CONTRACTPAYMENT
        if entity_name == 'Ticketpayment':
            return Entity.TICKETPAYMENT
        raise Exception('Entity enum %s not recognized' % entity_name)

    @staticmethod
    def row2dict(r):
        row_dict = {}
        for c in r.__table__.columns:
            if getattr(r, c.name) is None:
                row_dict[c.name] = {'type': str(c.type)}
            else:
                row_dict[c.name] = {'data': str(getattr(r, c.name)),
                                    'type': str(c.type)}
        return row_dict


    @staticmethod
    def payment_params():
        return ['payment_token']

    @staticmethod
    def payment_token():
        return 'payment_token'

    def __init__(self, entity_name):
        self.entity = ActionExecutor.string2entity(entity_name)

    def query_all(self):
        data = []
        if self.entity == Entity.OWNER:
            data = [ActionExecutor.row2dict(entry)
                    for entry in Owner.query_all()]
        if self.entity == Entity.PROPERTY:
            data = [ActionExecutor.row2dict(entry)
                    for entry in Property.query_all()]
        if self.entity == Entity.MANAGER:
            data = [ActionExecutor.row2dict(entry)
                    for entry in Manager.query_all()]
        if self.entity == Entity.TENANT:
            data = [ActionExecutor.row2dict(entry)
                    for entry in Tenant.query_all()]
        if self.entity == Entity.TICKET:
            data = [ActionExecutor.row2dict(entry)
                    for entry in Ticket.query_all()]
        if self.entity == Entity.UNIT:
            data = [ActionExecutor.row2dict(entry)
                    for entry in Unit.query_all()]
        if self.entity == Entity.CONTRACT:
            data = [ActionExecutor.row2dict(entry)
                    for entry in Contract.query_all()]
        if self.entity == Entity.CONTRACTOR:
            data = [ActionExecutor.row2dict(entry)
                    for entry in Contractor.query_all()]
        if self.entity == Entity.CONTRACTPAYMENT:
            data = [ActionExecutor.row2dict(entry)
                    for entry in ContractPayment.query_all()]
        if self.entity == Entity.TICKETPAYMENT:
            data = [ActionExecutor.row2dict(entry)
                    for entry in TicketPayment.query_all()]
        return data

    def create(self, payload):
        entry = None
        if self.entity == Entity.OWNER:
            if not Owner.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            owner = Owner.create(**payload)
            entry = ActionExecutor.row2dict(owner)
        if self.entity == Entity.PROPERTY:
            if not Property.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            entry = ActionExecutor.row2dict(Property.create(**payload))
        if self.entity == Entity.MANAGER:
            if not Manager.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            entry = ActionExecutor.row2dict(Manager.create(**payload))
        if self.entity == Entity.TENANT:
            if not Tenant.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            tenant = Tenant.create(**payload)
            entry = ActionExecutor.row2dict(tenant)
        if self.entity == Entity.TICKET:
            if not Ticket.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            entry = ActionExecutor.row2dict(Ticket.create(**payload))
        if self.entity == Entity.UNIT:
            if not Unit.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            entry = ActionExecutor.row2dict(Unit.create(**payload))
        if self.entity == Entity.CONTRACT:
            if not Contract.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            entry = ActionExecutor.row2dict(Contract.create(**payload))
        if self.entity == Entity.CONTRACTOR:
            if not Contractor.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            entry = ActionExecutor.row2dict(Contract.create(**payload))
        if self.entity == Entity.CONTRACTPAYMENT:
            if not ContractPayment.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            entry = ActionExecutor.row2dict(Transaction.create(**payload))
        if self.entity == Entity.TICKETPAYMENT:
            if not TicketPayment.dict_has_all_required_keys(payload):
                raise Exception('Entity %s was not supplied a complete payload for construction' %
                                ActionExecutor.entity2string(self.entity))
            entry = ActionExecutor.row2dict(Transaction.create(**payload))
        if entry is None:
            raise Exception('Create semantics for %s are undefined' %
                            ActionExecutor.entity2string(self.entity))
        Db.session.commit()
        return entry

    def update(self, payload):
        entry = None
        if self.entity == Entity.OWNER:
            entry = Owner.query_by_id(payload['id'])
        if self.entity == Entity.PROPERTY:
            entry = Property.query_by_id(payload['id'])
        if self.entity == Entity.MANAGER:
            entry = Manager.query_by_id(payload['id'])
        if self.entity == Entity.TENANT:
            entry = Tenant.query_by_id(payload['id'])
        if self.entity == Entity.TICKET:
            entry = Ticket.query_by_id(payload['id'])
        if self.entity == Entity.UNIT:
            entry = Unit.query_by_id(payload['id'])
        if self.entity == Entity.CONTRACT:
            entry = Contract.query_by_id(payload['id'])
        if self.entity == Entity.CONTRACTOR:
            entry = Contractor.query_by_id(payload['id'])
        if self.entity == Entity.CONTRACTPAYMENT:
            entry = ContractPayment.query_by_id(payload['id'])
        if self.entity == Entity.TICKETPAYMENT:
            entry = TicketPayment.query_by_id(payload['id'])
        if entry is None:
            raise Exception('Update semantics for %s are undefined' %
                            ActionExecutor.entity2string(self.entity))
        api_payload = {prop: payload[prop]
                       for prop in payload if prop not in ActionExecutor.payment_params()}
        entry.copy_from_dict(api_payload)
        Db.session.commit()
        payment_keys = set([ActionExecutor.payment_token()])
        if self.entity == Entity.PROPERTY and payment_keys.issubset(set(payload.keys())):
            print 'Update request for Property includes payment details, initializing payment info...'
            entry.create_payments(payload[ActionExecutor.payment_token()])
            Db.session.commit()
        if self.entity == Entity.TENANT and payment_keys.issubset(set(payload.keys())):
            print 'Update request for Tenant includes payment details, initializing payment info...'
            entry.create_payments(payload[ActionExecutor.payment_token()])
            Db.session.commit()
        if self.entity == Entity.CONTRACTOR and payment_keys.issubset(set(payload.keys())):
            print 'Update request for Contractor includes payment details, initializing payment info...'
            entry.create_payments(payload[ActionExecutor.payment_token()])
            Db.session.commit()
        return ActionExecutor.row2dict(entry)
