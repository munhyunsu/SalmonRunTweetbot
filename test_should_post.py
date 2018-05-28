from main import should_post

import datetime

def test_should_post():
    now = datetime.datetime(year=2018, month=5, day=28, hour=15, minute=0, second=0)
    notice = datetime.datetime(year=2018, month=5, day=28, hour=15, minute=0, second=0)

    texts = ['[시작] 공지가 {0}일 때: {1} 부터 {2} 사이에 실행되면 업로드',
             '[예정] 공지가 {0}일 때: {1} 부터 {2} 사이에 실행되면 업로드',
             '[끝] 공지가 {0}일 때: {1} 부터 {2} 사이에 실행되면 업로드']

    for index in range(0, 3):
        ptr = notice - datetime.timedelta(days=1)
        while should_post(notice, notice, ptr)[0] == False:
            ptr = ptr + datetime.timedelta(seconds=1)
        start_ptr = ptr
        while should_post(notice, notice, ptr)[0] == True:
            ptr = ptr + datetime.timedelta(seconds=1)
        end_ptr = ptr
        print(texts[index].format(notice, start_ptr, end_ptr))

    # ptr = now - datetime.timedelta(days=1)
    # while should_post(notice, notice, ptr)[1] == False:
    #     ptr = ptr + datetime.timedelta(seconds=1)
    # start_ptr = ptr
    # while should_post(notice, notice, ptr)[1] == True:
    #     ptr = ptr + datetime.timedelta(seconds=1)
    # end_ptr = ptr
    # print(notice, start_ptr, end_ptr)
    #
    # ptr = now - datetime.timedelta(days=1)
    # while should_post(notice, notice, ptr)[2] == False:
    #     ptr = ptr + datetime.timedelta(seconds=1)
    # start_ptr = ptr
    # while should_post(notice, notice, ptr)[2] == True:
    #     ptr = ptr + datetime.timedelta(seconds=1)
    # end_ptr = ptr
    # print(notice, start_ptr, end_ptr)

test_should_post()
# print(should_post(datetime.datetime.now(),datetime.datetime.now()))