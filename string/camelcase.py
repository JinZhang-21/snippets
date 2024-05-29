from re import sub

def camel(s):
    # Use str.title() to capitalize the first letter of each word and convert the rest to lowercase.
    s = sub(r'(_|-)+', " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])

camel('some_database_field_name') # 'someDatabaseFieldName'
camel('Some label that needs to be camelized')
# 'someLabelThatNeedsToBeCamelized'
camel('some-javascript-property') # 'someJavascriptProperty'
camel('some-mixed_string with spaces_underscores-and-hyphens')
# 'someMixedStringWithSpacesUnderscoresAndHyphens'