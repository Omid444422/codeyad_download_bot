from glob import glob
from json import loads
from os import makedirs,path
from requests import get

json_files = glob('./*.json')
json_list = None

for json_file in json_files:
    with open(json_file,'r',encoding='utf-8') as current_json_file:
        json_list = loads(current_json_file.read())

        
        file_name = json_file.replace('.\\','').split('.')
        course_name = file_name[0]
        counter = 0

        print(course_name)

        if not path.isdir(course_name):
            makedirs(course_name)

        for json_data in json_list:
            dir_name = json_data['name'].replace(':',' ').replace('|',' ').replace('*',' ').replace('"',' ').replace('/',' ').replace('\\',' ').replace('?',' ')

            if not path.isdir(course_name +'\\'+ dir_name):
                makedirs(course_name +'\\'+ dir_name)

            for url in json_data['urls']:
                name = url['name'].replace(':',' ').replace('|',' ').replace('*',' ').replace('"',' ').replace('/',' ').replace('\\',' ').replace('?',' ')

                counter += 1

                if(path.isfile(course_name + '\\'+dir_name+'\\'+ str(counter) + '_' + name + '.mp4')):
                    print('skip: ' + name )
                    print('current number: ' + str(counter))
                    continue
                
                download_video = get(url['url'])
                
                file = open('./' + course_name + '/'+dir_name+'/'+ str(counter) + '_' + name + '.mp4','wb')
                file.write(download_video.content)
                file.close()

                print(name + ' downloaded')

        print('*' * 150)
        print(course_name)


                