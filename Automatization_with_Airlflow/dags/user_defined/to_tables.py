import pandas as pd
import numpy as np
import pickle



def load_data(file):
    df = pd.read_csv(file)
    return df



def get_gender_dict():
    gender_dict = {
        'Man': 'Male', 
        'Prefer not to say':'Prefer not to say', 
        'Woman': 'Female',
        'Non-binary, genderqueer, or gender non-conforming': 'Non-binary',
        'Man;Non-binary, genderqueer, or gender non-conforming':'Male;Transgender',
        'Woman;Non-binary, genderqueer, or gender non-conforming':'Female;Transgender',
        'Or, in your own words:;Woman;Non-binary, genderqueer, or gender non-conforming':'Female;Transgender',
        'Or, in your own words:':'Prefer not to say', 
        'Man;Or, in your own words:':'Prefer not to say',
        'Or, in your own words:;Woman':'Female',
        'Man;Or, in your own words:;Woman;Non-binary, genderqueer, or gender non-conforming':'Non-binary',
        'Man;Woman;Non-binary, genderqueer, or gender non-conforming': 'Non-binary',
        'Or, in your own words:;Non-binary, genderqueer, or gender non-conforming':'Non-binary',
        'Man;Woman':'Non-binary'
    }
    return gender_dict


def normalize_gender(df:pd.DataFrame, get_gender_dict):


    df['Gender'].fillna('Prefer not to say', inplace=True)
    gender_dict = get_gender_dict()
    df['Gender'] = df['Gender'].map(gender_dict)

    return df


def normalize_sexuality(df:pd.DataFrame):
    df['Sexuality'].fillna('Prefer not to say', inplace=True)
    df['Sexuality'].replace('Straight or heterosexual','Straight',inplace=True)
    df['Sexuality'].replace('Bisexual or Queer','Bisexual',inplace=True)
    df['Sexuality'].replace('Gay or Lesbian','Gay',inplace=True)
    df['Sexuality'].replace('Straight or heterosexual;Bisexual or Queer','Others',inplace=True)
    df['Sexuality'].replace('Straight or heterosexual;Asexual', 'Others',inplace=True)
    df['Sexuality'].replace('Asexual', 'Others',inplace=True)

    df['Sexuality'].replace('Gay or Lesbian;Bisexual or Queer', 'Gay',inplace=True)
    df['Sexuality'].replace('Bisexual or Queer;Asexual', 'Others',inplace=True)
    df['Sexuality'].replace('Straight or heterosexual;Gay or Lesbian;Bisexual or Queer;Asexual', 'Others',inplace=True)
    df['Sexuality'].replace('Straight or heterosexual;Gay or Lesbian;Bisexual or Queer', 'Others',inplace=True)
    df['Sexuality'].replace('Straight or heterosexual;Gay or Lesbian','Others',inplace=True)
    df['Sexuality'].replace('Straight or heterosexual;Bisexual or Queer;Asexual','Others',inplace=True)       ,
    df['Sexuality'].replace('Gay or Lesbian;Asexual','Others',inplace=True)
    df['Sexuality'].replace('Gay or Lesbian;Bisexual or Queer;Asexual','Others',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual', 'Bisexual',inplace=True) 
    df['Sexuality'].replace('Bisexual;Straight / Heterosexual', 'Others',inplace=True)
    df['Sexuality'].replace('Bisexual;Gay or Lesbian', 'Gay',inplace=True)

    df['Sexuality'].replace('Bisexual;Gay or Lesbian;Straight / Heterosexual','Others',inplace=True) 
    df['Sexuality'].replace('Gay or Lesbian;Straight / Heterosexual','Others',inplace=True) 
    df['Sexuality'].replace('Bisexual;Queer','Gay',inplace=True) 
    df['Sexuality'].replace('Bisexual;Queer','Gay',inplace=True) 


    df['Sexuality'].replace('Gay or Lesbian;Queer','Gay',inplace=True) 
    df['Sexuality'].replace('Queer','Gay',inplace=True) 
    df['Sexuality'].replace('Bisexual;Gay or Lesbian;Straight / Heterosexual;Queer','Others',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual;Queer','Others',inplace=True) 
    df['Sexuality'].replace('Bisexual;Gay or Lesbian;Queer','Gay',inplace=True) 
    df['Sexuality'].replace('Bisexual;Straight / Heterosexual;Queer','Others',inplace=True) 

    df['Sexuality'].replace('Straight / Heterosexual;Bisexual;Gay or Lesbian;Queer','Others',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual;Prefer to self-describe:','Straight',inplace=True) 
    df['Sexuality'].replace('Prefer to self-describe:','Prefer not to say',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual;Bisexual','Bisexual',inplace=True) 

    df['Sexuality'].replace('Prefer to self-describe:;Queer','Gay',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual;Bisexual;Gay or Lesbian','Others',inplace=True) 
    df['Sexuality'].replace('Bisexual;Prefer to self-describe:','Bisexual',inplace=True) 
    df['Sexuality'].replace('Bisexual;Prefer to self-describe:;Queer','Gay',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual;Gay or Lesbian','Others',inplace=True) 


    df['Sexuality'].replace('Bisexual;Prefer to self-describe:;Gay or Lesbian;Queer','Gay',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual;Bisexual;Queer','Others',inplace=True) 
    df['Sexuality'].replace('Prefer to self-describe:;Gay or Lesbian;Queer','Gay',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual;Bisexual;Prefer to self-describe:;Gay or Lesbian;Queer','Others',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual;Bisexual;Prefer to self-describe:','Bisexual',inplace=True) 


    df['Sexuality'].replace('Prefer to self-describe:;Gay or Lesbian','Gay',inplace=True) 

    df['Sexuality'].replace('Straight / Heterosexual;Prefer to self-describe:;Queer','Others',inplace=True) 
    df['Sexuality'].replace('Bisexual;Prefer to self-describe:;Gay or Lesbian','Gay',inplace=True) 
    df['Sexuality'].replace('Bisexual;Straight / Heterosexual;Gay or Lesbian;Queer','Others',inplace=True) 
    df['Sexuality'].replace('Bisexual;Straight / Heterosexual;Gay or Lesbian','Others',inplace=True) 

    df['Sexuality'].replace('Bisexual;Straight / Heterosexual;Prefer to self-describe:;Gay or Lesbian;Queer','Others',inplace=True) 
    df['Sexuality'].replace('Bisexual;Straight / Heterosexual;Prefer to self-describe:','Others',inplace=True) 
    df['Sexuality'].replace('Straight / Heterosexual;Prefer to self-describe:;Gay or Lesbian','Others',inplace=True) 

    return df



def get_dev_table(df:pd.DataFrame, idplus_dict):
    
    idplus = idplus_dict['dev_df']

    n_rows = df.shape[0]
    id = np.arange(idplus, n_rows+idplus)
    
    dev_df = df[['Age', 'Gender', 'Sexuality', 'Ethnicity', 'EdLevel','SurveyYear']]
    
    dev_df.insert(0, 'id_dev', dev_df['SurveyYear']*1000000+id, True)
    dev_df.insert(7, 'id_job', id, True)
    dev_df.insert(8, 'id_exp', id, True)

    dev_df = dev_df.rename(columns=str.lower)

    return dev_df


def get_job_table(df:pd.DataFrame, idplus_dict):

    idplus = idplus_dict['job_df']
    n_rows = df.shape[0]
    id = np.arange(idplus, n_rows+idplus)
    
    job_df = df[['CompanySize', 'Country', 'Employment', 'Currency',
        'CurrencySymbol', 'Salary', 'SalaryFreq', 'DollarizedSalary']]

    job_df.insert(0, 'id_job', id, True)
    # job_df.insert(9, 'id_dev_type', id, True)

    job_df = job_df.rename(columns=str.lower)

    return job_df


def get_exp_table(df:pd.DataFrame, idplus_dict):

    idplus = idplus_dict['exp_df']
    n_rows = df.shape[0]
    id = np.arange(idplus, n_rows+idplus)
    
    exp_df = df[['YearsCode', 'YearsCodePro', 'OperatingSystem']]

    exp_df.insert(0, 'id_exp', id, True)

    exp_df = exp_df.rename(columns=str.lower)
    return exp_df


def col_with_semicolon_to_list_of_unique(df, col):
    """
        Transforms a column of data separated by semicolons into a list with the 
        unique values of the entire column.

        Input:
            df: Dataframe, Dataframe containing desired column
            col: String, name of the column

        Output:
            unique_values_list: list, list of unique values across the entire column
    """
    df_raw = df[col].copy()
    df_raw.dropna(inplace=True)
    df_raw = df_raw.unique().tolist()
    list_with_duplicates = []

    for x in df_raw:
        splitted = x.split(';')
        list_with_duplicates.append(splitted)

    # Plain data with comprehension list
    plain_list = [data for sublist in list_with_duplicates for data in sublist]

    # Unique values
    unique_values_set = set(plain_list)

    # Unique values list
    unique_values_list = list(unique_values_set)

    return unique_values_list



def get_unique_table(df:pd.DataFrame, table_name, column_name, idplus_dict, pickle_file, id_name, name):

    # table_name='lang_df'
    # column_name = 'LanguageHaveWorkedWith'

    # get value of next unique key
    idplus = idplus_dict[table_name]

    # get list of unique ocurrences
    unique_values = col_with_semicolon_to_list_of_unique(df, column_name )
    print("unique_values --> ", unique_values)
    
    # Get old dictionary
    if idplus !=0: 
        my_old_dict = load_generic_dict(pickle_file)
    else: # If not, create an empy dict
        my_old_dict = dict()
        
    
    # Check if unique_lang are in my_old_dict.keys()
    unique_values_set = set(unique_values)
    print("idplus --> ", idplus)
    if idplus !=0:
        unique_old_values_set = set(my_old_dict.keys())
    else:
        unique_old_values_set = set([])

    true_new_unique_values_set = unique_values_set.difference(unique_old_values_set)    

    true_new_unique_values = list(true_new_unique_values_set)
    true_new_unique_range = np.arange(idplus,idplus+len(true_new_unique_values))
    print("True_new_unique_lang --> ", true_new_unique_values)

    my_new_dict = my_old_dict.copy()
    if len(true_new_unique_values)>0:
        i = idplus
        for val in true_new_unique_values:
            my_new_dict[val] = i
            i+=1
        
    # Get number of ocurrences
    val_len = len(my_new_dict.items())

    
    val_idx = my_new_dict.values()
    val = my_new_dict.keys()

    # Create a new Dataframe for each 
    # val_df = pd.DataFrame({id_name:val_idx, name:true_new_unique_values})
    val_df = pd.DataFrame({id_name:val_idx, name:val})

    val_df = val_df.rename(columns=str.lower)

    save_generic_dict(my_new_dict, pickle_file)

    diff_df = pd.DataFrame({id_name: true_new_unique_range, name:true_new_unique_values})

    print("table_name --> ", table_name)
    print("diff_df --> \n", diff_df)
    print("------------------------------------------")
    print("val_df --> \n",val_df)
    return val_df, diff_df




def get_language_dict(lang_df:pd.DataFrame):
    # load old dictionary
    inv_lang_dict = lang_df['language'].to_dict()
    lang_dict = {v:k for k, v in inv_lang_dict.items()}

    return lang_dict



def get_database_dict(db_df:pd.DataFrame):
    
    inv_db_dict = db_df['database'].to_dict()
    db_dict = {v:k for k, v in inv_db_dict.items()}

    return db_dict



def get_framework_dict(framework_df:pd.DataFrame):
    
    inv_framework_dict = framework_df['framework'].to_dict()
    framework_dict = {v:k for k, v in inv_framework_dict.items()}

    return framework_dict


def get_platform_dict(platform_df:pd.DataFrame):
    
    inv_platform_dict = platform_df['platform'].to_dict()
    platform_dict = {v:k for k, v in inv_platform_dict.items()}

    return platform_dict




def get_devtype_dict(dev_type_df:pd.DataFrame):
    
    inv_dev_type_dict = dev_type_df['dev_type'].to_dict()
    dev_type_dict = {v:k for k, v in inv_dev_type_dict.items()}

    return dev_type_dict




def get_experience_language_table(df:pd.DataFrame, lang_df:pd.DataFrame, get_language_dict, idplus_dict, pickle_file):

    idplus = idplus_dict['df_exp_lang']
    idplus_exp = idplus_dict['exp_df']

    # lang_dict= get_language_dict(lang_df)
    lang_dict = load_generic_dict(pickle_file)


    df_exp_lang = df.assign(LanguageHaveWorkedWith=df['LanguageHaveWorkedWith'].str.split(';')).explode('LanguageHaveWorkedWith')
    df_exp_lang = df_exp_lang.reset_index().rename(columns={'index':'id'})
    df_exp_lang = df_exp_lang[['id','LanguageHaveWorkedWith']].drop_duplicates().reset_index(drop=True).sort_values('id')
    df_exp_lang = df_exp_lang.rename(columns={'LanguageHaveWorkedWith':'language'})
    df_exp_lang['id_lang'] = df_exp_lang['language'].map(lang_dict)


    df_exp_lang.drop(columns=['language'], inplace=True)
    df_exp_lang.rename(columns={'id':'id_exp'}, inplace=True)
    df_exp_lang.reset_index(inplace=True, drop=False)
    df_exp_lang.rename(columns={'index':'id_exp_lang'}, inplace=True)
    

    df_exp_lang = df_exp_lang.rename(columns=str.lower)
    df_exp_lang['id_exp_lang'] = df_exp_lang['id_exp_lang'] + idplus
    df_exp_lang['id_exp'] = df_exp_lang['id_exp'] + idplus_exp

    return df_exp_lang


def get_experience_database_table(df:pd.DataFrame, db_df:pd.DataFrame, get_database_dict, idplus_dict, pickle_file):
    
    idplus = idplus_dict['df_exp_db']
    idplus_exp = idplus_dict['exp_df']

    # db_dict = get_database_dict(db_df)
    db_dict = load_generic_dict(pickle_file)


    # Database
    df_exp_db = df.assign(DatabaseHaveWorkedWith=df['DatabaseHaveWorkedWith'].str.split(';')).explode('DatabaseHaveWorkedWith')
    df_exp_db = df_exp_db.reset_index().rename(columns={'index':'id'})
    df_exp_db = df_exp_db[['id','DatabaseHaveWorkedWith']].drop_duplicates().reset_index(drop=True).sort_values('id')
    df_exp_db = df_exp_db.rename(columns={'DatabaseHaveWorkedWith':'database'})
    df_exp_db['id_database'] = df_exp_db['database'].map(db_dict)


    df_exp_db.drop(columns=['database'], inplace=True)
    df_exp_db.reset_index(inplace=True, drop=False)
    df_exp_db.rename(columns={'id':'id_exp', 'index':'id_exp_db'}, inplace=True)
    # df_exp_db.head()

    df_exp_db = df_exp_db.rename(columns=str.lower)
    df_exp_db['id_exp_db'] = df_exp_db['id_exp_db'] + idplus
    df_exp_db['id_exp'] = df_exp_db['id_exp'] + idplus_exp

    return df_exp_db


def get_experience_framework_table(df:pd.DataFrame, framework_df:pd.DataFrame, get_framework_dict, idplus_dict, pickle_file):

    idplus = idplus_dict['df_exp_framework']
    idplus_exp = idplus_dict['exp_df']

    # framework_dict = get_framework_dict(framework_df)
    framework_dict = load_generic_dict(pickle_file)


    # Framework
    df_exp_framework = df.assign(FrameworkHaveWorkedWith=df['FrameworkHaveWorkedWith'].str.split(';')).explode('FrameworkHaveWorkedWith')
    df_exp_framework = df_exp_framework.reset_index().rename(columns={'index':'id'})
    df_exp_framework = df_exp_framework[['id','FrameworkHaveWorkedWith']].drop_duplicates().reset_index(drop=True).sort_values('id')
    df_exp_framework = df_exp_framework.rename(columns={'FrameworkHaveWorkedWith':'framework'})
    df_exp_framework['id_framework'] = df_exp_framework['framework'].map(framework_dict)

    df_exp_framework.drop(columns=['framework'], inplace=True)
    df_exp_framework.reset_index(inplace=True, drop=False)
    df_exp_framework.rename(columns={'id':'id_exp', 'index':'id_exp_framework'}, inplace=True)
    
    df_exp_framework = df_exp_framework.rename(columns=str.lower)
    df_exp_framework['id_exp_framework'] = df_exp_framework['id_exp_framework'] + idplus
    df_exp_framework['id_exp'] = df_exp_framework['id_exp'] + idplus_exp

    return df_exp_framework


def get_experience_platform_table(df:pd.DataFrame, platform_df:pd.DataFrame, get_platform_dict, idplus_dict, pickle_file):

    idplus = idplus_dict['df_exp_platform']
    idplus_exp = idplus_dict['exp_df']

    # platform_dict = get_platform_dict(platform_df)
    platform_dict = load_generic_dict(pickle_file)

    # Platform
    df_exp_platform = df.assign(PlatformHaveWorkedWith=df['PlatformHaveWorkedWith'].str.split(';')).explode('PlatformHaveWorkedWith')
    df_exp_platform = df_exp_platform.reset_index().rename(columns={'index':'id'})
    df_exp_platform = df_exp_platform[['id','PlatformHaveWorkedWith']].drop_duplicates().reset_index(drop=True).sort_values('id')
    df_exp_platform = df_exp_platform.rename(columns={'PlatformHaveWorkedWith':'platform'})
    df_exp_platform['id_platform'] = df_exp_platform['platform'].map(platform_dict)
    df_exp_platform.drop(columns=['platform'], inplace=True)
    df_exp_platform.reset_index(inplace=True, drop=False)
    df_exp_platform.rename(columns={'id':'id_exp', 'index':'id_exp_platform'}, inplace=True)
    df_exp_platform.head()


    df_exp_platform = df_exp_platform.rename(columns=str.lower)
    df_exp_platform['id_exp_platform'] = df_exp_platform['id_exp_platform'] + idplus
    df_exp_platform['id_exp'] = df_exp_platform['id_exp'] + idplus_exp

    return df_exp_platform



def get_job_devtype_table(df:pd.DataFrame, dev_type_df:pd.DataFrame, get_devtype_dict, idplus_dict, pickle_file):
    
    idplus = idplus_dict['df_job_devtype']
    idplus_exp = idplus_dict['exp_df']
    # dev_type_dict  = get_devtype_dict(dev_type_df)
    dev_type_dict = load_generic_dict(pickle_file)

    # DevType(Position) --> preprocessing    
    df.rename(columns={'DevType(Position)':'dev_type'}, inplace=True)
    # dev_type

    df_job_devtype = df.assign(dev_type=df['dev_type'].str.split(';')).explode('dev_type')
    df_job_devtype = df_job_devtype.reset_index().rename(columns={'index':'id'})
    df_job_devtype = df_job_devtype[['id','dev_type']].drop_duplicates().reset_index(drop=True).sort_values('id')
    df_job_devtype['id_dev_type'] = df_job_devtype['dev_type'].map(dev_type_dict)

    df_job_devtype.drop(columns=['dev_type'], inplace=True)
    df_job_devtype.reset_index(inplace=True, drop=False)
    df_job_devtype.rename(columns={'id':'id_job', 'index':'id_job_devtype'}, inplace=True)
    df_job_devtype.head()

    df_job_devtype = df_job_devtype.rename(columns=str.lower)
    df_job_devtype['id_job_devtype'] = df_job_devtype['id_job_devtype'] + idplus
    df_job_devtype['id_job'] = df_job_devtype['id_job'] + idplus_exp

    return df_job_devtype


def load_idplus_dict_all_cases(pickle_file,load_init=False):

    if load_init:
        idplus_dict = load_init_idplus(pickle_file)
    else:
        idplus_dict = load_idplus_dict(pickle_file)

    return idplus_dict


def get_all_tables(file,  pickle_file, lang_pk, db_pk, fm_pk, plt_pk, dt_pk, load_init=False):
    
    idplus_dict = load_idplus_dict_all_cases(pickle_file,load_init)


    df= load_data(file)
    df = normalize_gender(df, get_gender_dict)
    df = normalize_sexuality(df)

    dev_df = get_dev_table(df, idplus_dict)
    job_df = get_job_table(df, idplus_dict)
    exp_df = get_exp_table(df, idplus_dict)

    # Language_picle_file = '../data/test/language.pickle'
    lang_df, diff_lang_df = get_unique_table(df, 'lang_df', 'LanguageHaveWorkedWith', idplus_dict, lang_pk, 'id_lang', 'language')
    
    # db_pickle_file = '../data/test/database.pickle'
    db_df, diff_db_df = get_unique_table(df, 'db_df', 'DatabaseHaveWorkedWith', idplus_dict, db_pk, 'id_db', 'database')
    
    # framework_pickle = '../data/test/framework.pickle'
    framework_df, diff_framework_df = get_unique_table(df, 'framework_df', 'FrameworkHaveWorkedWith', idplus_dict, fm_pk, 'id_framework', 'framework')
    
    # platform_pickle = '../data/test/platform.pickle'
    platform_df, diff_platform_df = get_unique_table(df, 'platform_df', 'PlatformHaveWorkedWith', idplus_dict, plt_pk, 'id_platform', 'platform')

    # dev_type_pickle = '../data/test/dev_type.pickle'
    dev_type_df, diff_dev_type_df = get_unique_table(df, 'dev_type_df', 'DevType(Position)', idplus_dict, dt_pk, 'id_dev_type', 'dev_type')
    
    df_exp_lang = get_experience_language_table(df, lang_df, get_language_dict, idplus_dict, lang_pk)
    df_exp_db = get_experience_database_table(df, db_df, get_database_dict, idplus_dict, db_pk)
    df_exp_framework = get_experience_framework_table(df, framework_df, get_framework_dict, idplus_dict, fm_pk)
    df_exp_platform = get_experience_platform_table(df, platform_df, get_platform_dict, idplus_dict, plt_pk)
    df_job_devtype = get_job_devtype_table(df, dev_type_df, get_devtype_dict, idplus_dict, dt_pk)

    df_list = dev_df, job_df, exp_df, lang_df, db_df, framework_df, platform_df, dev_type_df,\
        df_exp_lang, df_exp_db, df_exp_framework, df_exp_platform, df_job_devtype 
    update_idplus_dict(df_list, idplus_dict, pickle_file)

    return df, dev_df, job_df, exp_df, diff_lang_df, diff_db_df, diff_framework_df, diff_platform_df, diff_dev_type_df, df_exp_lang, df_exp_db, df_exp_framework, df_exp_platform, df_job_devtype



def load_init_idplus(pickle_file):
    # For the first time saving to db, dictionary must be empty
    idplus_init_dict = {
        'dev_df': 0,
        'job_df': 0,
        'exp_df': 0,
        'lang_df': 0,
        'db_df': 0,
        'framework_df': 0,
        'platform_df': 0,
        'dev_type_df': 0,
        'df_exp_lang': 0,
        'df_exp_db': 0,
        'df_exp_framework': 0,
        'df_exp_platform': 0,
        'df_job_devtype': 0
    }
    
    with open(pickle_file, 'wb') as handle:
        pickle.dump(idplus_init_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return idplus_init_dict

def load_generic_dict(pickle_file):
    # Load picke_file containing idplus_dictionary
    with open(pickle_file, 'rb') as handle:
        my_dict = pickle.load(handle)
    
    return my_dict


def save_generic_dict(my_dict, pickle_file):
    with open(pickle_file, 'wb') as handle:
        pickle.dump(my_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)



def load_idplus_dict(pickle_file):
    # Load picke_file containing idplus_dictionary
    with open(pickle_file, 'rb') as handle:
        idplus_dict = pickle.load(handle)
    
    return idplus_dict


def update_idplus_dict(df_list, idplus_dict, pickle_file):

    # Load dataframe list
    dev_df, job_df, exp_df, lang_df, db_df, framework_df, platform_df, dev_type_df,\
        df_exp_lang, df_exp_db, df_exp_framework, df_exp_platform, df_job_devtype = df_list
    

    # Update dictionary
    idplus_dict['dev_df'] = idplus_dict['dev_df'] + dev_df.shape[0]
    idplus_dict['job_df'] = idplus_dict['job_df'] + job_df.shape[0]
    idplus_dict['exp_df'] = idplus_dict['exp_df'] + exp_df.shape[0]
    idplus_dict['lang_df'] = idplus_dict['lang_df'] + lang_df.shape[0]
    idplus_dict['db_df'] = idplus_dict['db_df'] + db_df.shape[0]
    idplus_dict['framework_df'] = idplus_dict['framework_df'] + framework_df.shape[0]
    idplus_dict['platform_df'] = idplus_dict['platform_df'] + platform_df.shape[0]
    idplus_dict['dev_type_df'] = idplus_dict['dev_type_df'] + dev_type_df.shape[0]
    idplus_dict['df_exp_lang'] = idplus_dict['df_exp_lang'] + df_exp_lang.shape[0]
    idplus_dict['df_exp_db'] = idplus_dict['df_exp_db'] + df_exp_db.shape[0]
    idplus_dict['df_exp_framework'] = idplus_dict['df_exp_framework'] + df_exp_framework.shape[0]
    idplus_dict['df_exp_platform'] = idplus_dict['df_exp_platform'] + df_exp_platform.shape[0]
    idplus_dict['df_job_devtype'] = idplus_dict['df_job_devtype'] + df_job_devtype.shape[0]

    # Save dictionary for next session
    with open(pickle_file, 'wb') as handle:
        pickle.dump(idplus_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def test_module():
    print("Module is ok")