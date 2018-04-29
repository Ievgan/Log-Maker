infile = open('token_2.dat', 'r')
outfile = open('log.dat', 'w')

#This function looks through token.dat file and creates a unique filename
def createFilename():
    setcount = [0, 0, 0, 0]
    setstr = ['', '', '', '']
    board_count, sernum_count, result_count, stoptime_count = setcount
    filename, sernum, result, stoptime = setstr
    split_tmp1, split_tmp2 = [[], []]

    for line in infile:
        test_sernum = line.startswith('    (USER:  SN: ')
        test_result = line.startswith('    (USER:  RESULT :')
        test_stoptime = line.startswith('    (USER:  STOP TIME :')

        if test_sernum:
            sernum = line[-20:-2]
            #print(serNum, file = outfile, end='')
            sernum_count += 1
            board_count += 1

        if test_result:
            result = line[-6:-2]
            result_count += 1

        if test_stoptime:
            stoptime_date = line[-30:-20]
            split_tmp1 = stoptime_date.split('/')
            stoptime_time = line[-19:-10]
            split_tmp2 = stoptime_time.split(':')

            stoptime = split_tmp1[0] + '_' + split_tmp1[1] + '_' + split_tmp1[2] + '_' + split_tmp2[0] + '_' + split_tmp2[1] + '_' + split_tmp2[2]
            #print(stoptime)
            stoptime_count += 1

        if sernum_count==result_count==stoptime_count==board_count==1:
            filename = str(result) + '_' + str(sernum) + '_' + str(board_count) + '_' + str(stoptime)
            print(sernum, result, stoptime, filename, sep='\n', end='\n\n', file=outfile)
            board_count, sernum_count, result_count, stoptime_count = [0, 0, 0, 0]

createFilename()
print('Done.')
