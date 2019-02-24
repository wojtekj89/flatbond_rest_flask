from ukpostcodeutils import validation

def validate_postcode(postcode):
    """ Using https://pypi.org/project/uk-postcode-utils/ for UK postcode validation """
    return validation.is_valid_postcode(postcode.upper())
    

def validate_fee(config, rent, fee):
    if config:
        if config.get('fixed_membership_fee'):
            membership = config.get('fixed_membership_amount') * 1.2
            return membership == fee
    
    minimum = 120 * 1.2 * 100 # 120 GBP + 20% VAT in pences
    membership_fee = max(round(rent * 1.2), minimum)
    return membership_fee == fee

def validate_rent(rent):
    return rent >= 2500 and rent <= 200000