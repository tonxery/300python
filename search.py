#!/usr/bin/env python
while True:
        input = raw_input("Please input your username:")
        if input == 'Alex':
                password = raw_input("please input your pass:")
                p = '123'
                while password != p:
                        password =raw_input("Wrong passwd,input again:" )
                else:
                        print 'Welcome login to TriAquae!\n'
                        while True:
                                match_yes = 0
                                input = raw_input("\033[32mPlease input the name whom you want to search:\033[0m")
                                contact_file = file('contact_list.txt')
                                while len(input) == 0 or input == " ":
                                        input = raw_input("\033[32mPlease input the name whom you want to search:\033[0m")
                                while True:
                                        line = contact_file.readline()
                                        if len(line) == 0:break
                                        if input in line:
                                                print 'Match item: \033[36;1m%s\033[0m' % line,
                                                match_yes = 1
                                        else:
                                                pass
                                if match_yes == 0 :print 'No match item found.'
        else:
                print "Sorry, user %s not found" % input