def set_viloyat(viloyat):
    if viloyat=='toshkent':
        return "tashkent"
    elif viloyat=='jizzax':
        return "jizzakh"
    elif viloyat=='andijon':
        return "andijan"
    elif viloyat=='farg\'ona' or viloyat=='fargona':
        return 'ferghana'
    elif viloyat=='gulison' or viloyat=='sirdaryo':
        return "gulistan"
    elif viloyat=='buxoro':
        return "bukhara"
    elif viloyat=='zarafshon':
        return 'zarafshan'
    elif viloyat=='qarshi' or viloyat=='qashqadaryo':
        return "karshi"
    elif viloyat=='navoiy':
        return 'navoi'
    elif viloyat=='qoraqalpogiston' or viloyat=='qoraqalpog\'iston':
        return 'nukus'
    elif viloyat=='termiz' or viloyat=='surxondaryo':
        return 'termez'
    elif viloyat=='urganch' or viloyat=='xorazm':
        return 'urgench'
    elif viloyat=='xiva':
        return 'khiva'
    elif viloyat=='samarqand':
        return 'samarkand'
    else:
        return viloyat