infile = open('token_2xpass.dat', 'r')
outfile = open('log.dat', 'w')

#This function looks through token.dat file and creates a unique filename
def createFilename():
    setcount = [0, False, False, False]
    setstr = ['', '', '', '']
    board_count, sernum_count, result_count, stoptime_count = setcount
    filename, sernum, result, stoptime = setstr


    for line in infile:
        test_sernum = line.startswith('    (USER:  SN:')
        test_result = line.startswith('    (USER:  RESULT :')
        test_stoptime = line.startswith('    (USER:  STOP TIME :')


        if test_sernum:
            sernum = line[-20:-2]
            #print(serNum, file = outfile)
            sernum_count = True
            board_count += 1

        if test_result:
            result = line[-6:-2]
            result_count = True

        if test_stoptime:
            temp = line[-29:-19]
            print(temp, end='\n')
            split_date = temp.split('/')
            #print(split_date, end='\n')
            stoptime = split_date[0] + '_' + split_date[1] + '_' + split_date[2]

            temp = line[-18:-10]
            print(temp, end='\n')
            split_time = temp.split(':')
            #print(split_time, end='\n')
            stoptime += '_' + split_time[0] + '_' + split_time[1] + '_' + split_time[2]

            #print(stoptime)
            stoptime_count = True


        if sernum_count&result_count&stoptime_count:
            filename = str(result) + '_' + str(sernum) + '_' + str(board_count) + '_' + str(stoptime)
            print(sernum, result, stoptime, filename, sep='\n', end='\n\n', file=outfile)
            sernum_count, result_count, stoptime_count = [False, False, False]

createFilename()
print('Done.')
