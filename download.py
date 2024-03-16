from glob import glob
from json import loads
from os import system,makedirs

json_files = glob('./*.json')
json_list = None

for json_file in json_files:
    with open(json_file,'r',encoding='utf-8') as current_json_file:
        json_list = loads(current_json_file.read())

        
        file_name = json_file.replace('./','').replace('|',' ').split('.')
        course_name = file_name[0].replace(' ','_').replace('(','_').replace(')','_')
        counter = 0
        makedirs(course_name)

        for json_data in json_list:
            dir_name = json_data['name'].replace(' ','_').replace('(','_').replace(')','_')

            makedirs(course_name +'/'+ dir_name)

            for url in json_data['urls']:
                name = url['name'].replace(' ','_').replace('(','_').replace(')','_')
                system('curl --output ./' + course_name + '/'+dir_name+'/'+ str(counter) + '_' + name + '.mp4 ' + url['url'])
                counter += 1


                