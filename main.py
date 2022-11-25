#============================================================================
#   2021/12/24 
#   ავტორი: გიორგი რჩეულიშვილი                                           
#----------------------------------------------------------------------------
#   CSV ფაილის გარდამქმნელ-წამკითხველი                                     
#----------------------------------------------------------------------------
#   განმარტება:
#       CSV(Comma Separated Values) არის მძიმით გამოყოფილი ცვლადები,
#       რომლებიც ინახება უბრალო ტექსტურ ფაილში და წარმოადგენს
#       ერთგვარ მონაცემთა ბაზას, რომელსაც გააჩნია ჩაწერის სტანდარტი.
#       მაგ:
#           id, saxeli, gvari, asaki
#           1, giorgi, rcheulishvili, 19
#       შექმნის 'მონაცემთა ბაზას' სადაც პირველი სტრიქონი სვეტების 
#       დასახელებებს წარმოადენს და დანარჩენი სტრიქონები თვითონ მონაცემებს.
#
#   მეტი ინფორმაციის ნახვა შესაძლებელია Wikipedia-ზე:
#       https://en.wikipedia.org/wiki/Comma-separated_values
#
#=============================================================================

from tkinter import *
import PySimpleGUI as sg
import csv
import os

from PySimpleGUI.PySimpleGUI import WIN_CLOSED, WIN_X_EVENT


#პარამეტრები
sg.ChangeLookAndFeel('Dark Teal 2')
#ცვლადები
headers = []
data = []

#შეკითხვის ფანჯრის აგებულება
layout1 = [  [sg.Text('გახსენით CSV ფაილი: '), sg.Input(), sg.FileBrowse('არჩევა')],
            [sg.OK('დასრულება'), sg.CloseButton('გაუქმება')]
        ]

windowCsvOpen = sg.Window('მიმდინარეობს ფაილის გახსნა...', layout1)

while True:
    event, values = windowCsvOpen.read()
    #ამოწმებს თუ გახსნილი ფაილი არ არის .csv ფორმატში [დაუსრულებელი]
    data_path = values[0]
    if data_path != None:
        split_path = os.path.splitext(data_path) #split_path = ['გახსნილი ფაილის მისამართი', '.ფორმატი']
    else:
        windowCsvOpen.close()
        del windowCsvOpen
        break

    #შეამოწმებს თუ ფაილი არ შეესაბამება ".csv" ფორმატს და გამოიტანს შესაბამის შეცდომას
    if split_path[1] != '.csv':
            if event == 'გაუქმება':
                break
            #თუ ფაილის ტიპი არ შეესაბამება 'csv' ფაილს...
            elif data_path == '':
                sg.popup('ფაილის მისამართი არ შეიძლება იყოს ცარიელი.', 'სცადეთ თავიდან...', no_titlebar = True, grab_anywhere= True)
                continue
            sg.popup('ფაილი არ შეესაბამება ".csv" ფორმატს.','სცადეთ თავიდან...',  no_titlebar = True, grab_anywhere= True)
            continue
        

    #ხსნის მითითებულ csv ფაილს და ახარისხებს ინფორმაციას
    csvfile = open(values[0],'r+', newline = '')
    csvreader = csv.reader(csvfile, delimiter = ',')
    #ქმნის სათაურთა სიას პირველი ხაზიდან
    headers = next(csvreader)
    #ქმნის ინფორმაციათა სიას დანარჩენი ხაზებიდან
    for row in csvreader:
        data.append(row)
    
    else:
        #ცხრილის ფანჯრის აგებულება
        
        layout2 = [ 
            [sg.Table(data, headings=headers, justification='center',expand_x=True, expand_y=True , vertical_scroll_only= False,
                         auto_size_columns=True, key = '-TABLE-')]
                      
    ]
        windowCsvDisplay = sg.Window("გახსნილია "+values[0], layout2, grab_anywhere=False, auto_size_buttons=True,
                                     resizable=True, size=(800,600))
        print(data)
        while True:
            try:
                event, values = windowCsvDisplay.read()
                    
                if event == WIN_CLOSED:
                    windowCsvDisplay.close()
                    windowCsvOpen.close()
                    del windowCsvDisplay
                    del windowCsvOpen
                    break
            except Exception:
                pass
          
