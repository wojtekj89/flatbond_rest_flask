from ukpostcodeutils import validation

def validate_postcode(postcode):
    """ Using https://pypi.org/project/uk-postcode-utils/ for UK postcode validation """
    return validation.is_valid_postcode(postcode)
    

def validate_fee(args):
    return True