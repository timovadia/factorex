# encoding: utf-8

def is_factor(user):
    return hasattr(user, 'factor_user')

def is_contractor(user):
    return hasattr(user, 'contractor_user')
