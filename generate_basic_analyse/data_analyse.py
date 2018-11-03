import dataframe_loader.generate_data as data_loader
import matplotlib.pyplot as plt
import pandas as pd
plt.interactive(False)


def total_label_wiki4hei(output, label, translate):
    df_count = output.groupby(label).size()
    df_count = df_count.rename(translate)
    output2 = pd.DataFrame(df_count)
    output2.rename(columns={0: 'total'}, inplace=True)
    output2.plot.pie( y='total', title= label,  autopct='%1.1f%%')
    plt.savefig(label)
    print(label)
    print(output2)


def check_enj_by_age(output):
    output['ENJ1'] = pd.to_numeric(output['ENJ1'], errors='coerce')
    output['ENJ2'] = pd.to_numeric(output['ENJ2'], errors='coerce')
    categories = pd.qcut(output["AGE"], 4)
    result = pd.pivot_table(output, index=[categories] , values = ['ENJ1','ENJ2'])
    print('Perceived Enjoyment by age range')
    print(result)
    result.plot.bar(title='Age per ENJ', rot=0)
    plt.savefig('check_enj_by_age' )

    pass


def check_enj_by_age_and_sex(output):
    output['ENJ1'] = pd.to_numeric(output['ENJ1'], errors='coerce')
    output['ENJ2'] = pd.to_numeric(output['ENJ2'], errors='coerce')
    output.GENDER.replace( [1, 0], ['male', 'female'],inplace=True)
    categories = pd.qcut(output["AGE"], 4)
    result = pd.pivot_table(output, index=['GENDER', categories] , values = ['ENJ1','ENJ2'])
    print('Perceived Enjoyment by age range')
    print(result)
    result.unstack(level=0).plot.bar(title='Gender and age per ENJ', rot=0, subplots=True)
    plt.savefig('check_enj_by_age_and_sex')
    pass

def check_enj_by_wiki_user(output):
    output['ENJ1'] = pd.to_numeric(output['ENJ1'], errors='coerce')
    output['ENJ2'] = pd.to_numeric(output['ENJ2'], errors='coerce')
    output = output[output.USERWIKI !='?']
    output.USERWIKI.replace(['1', '0'], ['enrolled', 'non-enrolled'], inplace=True)
    result = pd.pivot_table(output, index=['USERWIKI'] , values = ['ENJ1','ENJ2'])
    print('Perceived Enjoyment by age range')
    print(result)
    result.unstack(level=0).plot.bar(title='User of Wiki per ENJ', rot=0, subplots=True)
    plt.savefig('check_enj_by_wiki_user')
    pass


output = data_loader.get_data_frame()
total_label_wiki4hei(output, translate={0:'male', 1:'female'}, label="GENDER")
total_label_wiki4hei(output, translate={
'1':'Arts & Humanities',  '2':'Sciences',
'3':'Health Sciences', '4':'Engineering & Architecture', '5':'Law & Politics'
}, label="DOMAIN")

total_label_wiki4hei(output, translate={
0:'Without',  1:'With'}, label="PhD")
check_enj_by_age(output)
check_enj_by_age_and_sex(output)
check_enj_by_wiki_user(output)