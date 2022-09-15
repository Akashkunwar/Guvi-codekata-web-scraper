import json
from pydoc import writedoc
import requests
import os

cookies = {
    '_gcl_au': '1.1.2052476519.1661299672',
    'MXCookie': 'MXCookie',
    '_ga_NSG5GX8MNW': 'GS1.1.1661299672.1.1.1661299782.0.0.0',
    '_ga': 'GA1.2.2020022182.1661299673',
    '__stp': '{visit:new,uuid:dba12eaf-7e5b-48b7-b004-460e38776f1d}',
    '__sts': '{sid:1661299672946,tx:1661299745442,url:https%3A%2F%2Fwww.guvi.com%2Fcourses,pet:1661299745442,set:1661299672946,pUrl:https%3A%2F%2Fwww.guvi.com%2Fsign-in,pPet:1661299735258,pTx:1661299735258}',
    '__stgeo': '0',
    '__stbpnenable': '0',
    '__stdf': '0',
    '_gid': 'GA1.2.942533324.1661299674',
    '_fbp': 'fb.1.1661299674798.2071180317',
    '_clck': 'pk5s33|1|f4a|0',
    '_clsk': '1glhtmh|1661299748177|3|1|b.clarity.ms/collect',
    'G_ENABLED_IDPS': 'google',
    '_gat': '1',
    '_cc_id': '30ae4a31b9be802386a3bf8c78d08679',
    'panoramaId_expiry': '1661904537266',
    'panoramaId': 'cd83b8c5d49866a0182dfa2604d716d53938c75bb29cded314f9e73ee60f3a60',
    '_gat_UA-53114947-1': '1',
    'USER_DATA': '%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_USER_EMAIL%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22b31c5cb1-2767-4d75-892d-2247e54422f1%22%2C%22deviceAdded%22%3Atrue%7D',
    'moe_uuid': 'b31c5cb1-2767-4d75-892d-2247e54422f1',
    'user_id': '1183806',
    'user_email': 'gnspda%40gmail.com',
    'usertype': '1',
    'mp_74656ccf168534edf5fa89bedde46fb3_mixpanel': '%7B%22distinct_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24device_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.guvi.com',
    'Alt-Used': 'www.guvi.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.guvi.com/code-kata',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_gcl_au=1.1.2052476519.1661299672; MXCookie=MXCookie; _ga_NSG5GX8MNW=GS1.1.1661299672.1.1.1661299782.0.0.0; _ga=GA1.2.2020022182.1661299673; __stp={visit:new,uuid:dba12eaf-7e5b-48b7-b004-460e38776f1d}; __sts={sid:1661299672946,tx:1661299745442,url:https%3A%2F%2Fwww.guvi.com%2Fcourses,pet:1661299745442,set:1661299672946,pUrl:https%3A%2F%2Fwww.guvi.com%2Fsign-in,pPet:1661299735258,pTx:1661299735258}; __stgeo=0; __stbpnenable=0; __stdf=0; _gid=GA1.2.942533324.1661299674; _fbp=fb.1.1661299674798.2071180317; _clck=pk5s33|1|f4a|0; _clsk=1glhtmh|1661299748177|3|1|b.clarity.ms/collect; G_ENABLED_IDPS=google; _gat=1; _cc_id=30ae4a31b9be802386a3bf8c78d08679; panoramaId_expiry=1661904537266; panoramaId=cd83b8c5d49866a0182dfa2604d716d53938c75bb29cded314f9e73ee60f3a60; _gat_UA-53114947-1=1; USER_DATA=%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_USER_EMAIL%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22b31c5cb1-2767-4d75-892d-2247e54422f1%22%2C%22deviceAdded%22%3Atrue%7D; moe_uuid=b31c5cb1-2767-4d75-892d-2247e54422f1; user_id=1183806; user_email=gnspda%40gmail.com; usertype=1; mp_74656ccf168534edf5fa89bedde46fb3_mixpanel=%7B%22distinct_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24device_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
    'myData': '{"type":"conceptCardDetails","authtoken":"02364c144fcdeabfe35e8168ffc8fb56cfc0b6bcdbf98170599d7df0a277d6cc7063e527d5fb5d1b53282efa3df647417041d68348a6a3a85dc9e2a2916e8228","originUrl":"www.guvi.com"}',
}

response = requests.post('https://www.guvi.com/model/v2/codekataOperations.php', cookies=cookies, headers=headers, data=data)

categoryNames = []

categoriesArr = response.json()['overallData']

for category in categoriesArr:
    tempName = category['_id']
    categoryNames.append(tempName)
    # if tempName == 'Input/Output':
    #     try:
    #         os.mkdir('guvi/'+'IO')
    #     except:
    #         pass
    # else:
    #     try:
    #         os.mkdir('guvi/'+tempName+'/')
    #     except:
    #         pass

# exit()

cookies = {
    '_gcl_au': '1.1.2052476519.1661299672',
    'MXCookie': 'MXCookie',
    '_ga_NSG5GX8MNW': 'GS1.1.1661299672.1.1.1661299978.0.0.0',
    '_ga': 'GA1.2.2020022182.1661299673',
    '__stp': '{visit:new,uuid:dba12eaf-7e5b-48b7-b004-460e38776f1d}',
    '__sts': '{sid:1661299672946,tx:1661299919580,url:https%3A%2F%2Fwww.guvi.com%2Fcode-kata-main%3Fconcept%3Darray,pet:1661299919580,set:1661299672946,pUrl:https%3A%2F%2Fwww.guvi.com%2Fcode-kata,pPet:1661299783098,pTx:1661299783098}',
    '__stgeo': '0',
    '__stbpnenable': '0',
    '__stdf': '0',
    '_gid': 'GA1.2.942533324.1661299674',
    '_fbp': 'fb.1.1661299674798.2071180317',
    '_clck': 'pk5s33|1|f4a|0',
    '_clsk': '1glhtmh|1661299921034|6|1|b.clarity.ms/collect',
    'G_ENABLED_IDPS': 'google',
    '_cc_id': '30ae4a31b9be802386a3bf8c78d08679',
    'panoramaId_expiry': '1661904537266',
    'panoramaId': 'cd83b8c5d49866a0182dfa2604d716d53938c75bb29cded314f9e73ee60f3a60',
    'USER_DATA': '%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_USER_EMAIL%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22b31c5cb1-2767-4d75-892d-2247e54422f1%22%2C%22deviceAdded%22%3Atrue%7D',
    'moe_uuid': 'b31c5cb1-2767-4d75-892d-2247e54422f1',
    'user_id': '1183806',
    'user_email': 'gnspda%40gmail.com',
    'usertype': '1',
    'mp_74656ccf168534edf5fa89bedde46fb3_mixpanel': '%7B%22distinct_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24device_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
    '_gat_UA-53114947-1': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.guvi.com',
    'Alt-Used': 'www.guvi.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.guvi.com/code-kata-main?concept=array',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_gcl_au=1.1.2052476519.1661299672; MXCookie=MXCookie; _ga_NSG5GX8MNW=GS1.1.1661299672.1.1.1661299978.0.0.0; _ga=GA1.2.2020022182.1661299673; __stp={visit:new,uuid:dba12eaf-7e5b-48b7-b004-460e38776f1d}; __sts={sid:1661299672946,tx:1661299919580,url:https%3A%2F%2Fwww.guvi.com%2Fcode-kata-main%3Fconcept%3Darray,pet:1661299919580,set:1661299672946,pUrl:https%3A%2F%2Fwww.guvi.com%2Fcode-kata,pPet:1661299783098,pTx:1661299783098}; __stgeo=0; __stbpnenable=0; __stdf=0; _gid=GA1.2.942533324.1661299674; _fbp=fb.1.1661299674798.2071180317; _clck=pk5s33|1|f4a|0; _clsk=1glhtmh|1661299921034|6|1|b.clarity.ms/collect; G_ENABLED_IDPS=google; _cc_id=30ae4a31b9be802386a3bf8c78d08679; panoramaId_expiry=1661904537266; panoramaId=cd83b8c5d49866a0182dfa2604d716d53938c75bb29cded314f9e73ee60f3a60; USER_DATA=%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_USER_EMAIL%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22b31c5cb1-2767-4d75-892d-2247e54422f1%22%2C%22deviceAdded%22%3Atrue%7D; moe_uuid=b31c5cb1-2767-4d75-892d-2247e54422f1; user_id=1183806; user_email=gnspda%40gmail.com; usertype=1; mp_74656ccf168534edf5fa89bedde46fb3_mixpanel=%7B%22distinct_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24device_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _gat_UA-53114947-1=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

for category in categoryNames[::-1]:
    data = {
        'myData': '{"concept":"'+category+'","hash":"","authtoken":"02364c144fcdeabfe35e8168ffc8fb56cfc0b6bcdbf98170599d7df0a277d6cc7063e527d5fb5d1b53282efa3df647417041d68348a6a3a85dc9e2a2916e8228","originUrl":"www.guvi.com"}',
    }

    response = requests.post('https://www.guvi.com/model/v2/codekata/codekataFetchQuestions.php', cookies=cookies, headers=headers, data=data)

    completedQuestions = []

    completedQuestions = (response.json()['completionStatus']['completed'])
    completedQuestions = [int(x) for x in completedQuestions]
    availableQuestions = (json.loads(response.json()['questionData'])['questionOrder'])
    # print(availableQuestions)
    # break

    # print(completedQuestions)

    completedQuestionsInThisCategory = []

    for _ in availableQuestions:
        if _ in completedQuestions:
            completedQuestionsInThisCategory.append(_)
    
    completedQuestionsInThisCategory.sort()


    for completedQuestionID in completedQuestionsInThisCategory:

        cookies = {
    '_gcl_au': '1.1.2052476519.1661299672',
    'MXCookie': 'MXCookie',
    '_ga_NSG5GX8MNW': 'GS1.1.1661299672.1.1.1661299978.0.0.0',
    '_ga': 'GA1.2.2020022182.1661299673',
    '__stp': '{visit:new,uuid:dba12eaf-7e5b-48b7-b004-460e38776f1d}',
    '__sts': '{sid:1661299672946,tx:1661299919580,url:https%3A%2F%2Fwww.guvi.com%2Fcode-kata-main%3Fconcept%3Darray,pet:1661299919580,set:1661299672946,pUrl:https%3A%2F%2Fwww.guvi.com%2Fcode-kata,pPet:1661299783098,pTx:1661299783098}',
    '__stgeo': '0',
    '__stbpnenable': '0',
    '__stdf': '0',
    '_gid': 'GA1.2.942533324.1661299674',
    '_fbp': 'fb.1.1661299674798.2071180317',
    '_clck': 'pk5s33|1|f4a|0',
    '_clsk': '1glhtmh|1661299921034|6|1|b.clarity.ms/collect',
    'G_ENABLED_IDPS': 'google',
    '_cc_id': '30ae4a31b9be802386a3bf8c78d08679',
    'panoramaId_expiry': '1661904537266',
    'panoramaId': 'cd83b8c5d49866a0182dfa2604d716d53938c75bb29cded314f9e73ee60f3a60',
    'USER_DATA': '%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_USER_EMAIL%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22b31c5cb1-2767-4d75-892d-2247e54422f1%22%2C%22deviceAdded%22%3Atrue%7D',
    'moe_uuid': 'b31c5cb1-2767-4d75-892d-2247e54422f1',
    'user_id': '1183806',
    'user_email': 'gnspda%40gmail.com',
    'usertype': '1',
    'mp_74656ccf168534edf5fa89bedde46fb3_mixpanel': '%7B%22distinct_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24device_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
    '_gat_UA-53114947-1': '1',
}

        headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.guvi.com',
    'Alt-Used': 'www.guvi.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.guvi.com/code-kata-main?concept=array',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_gcl_au=1.1.2052476519.1661299672; MXCookie=MXCookie; _ga_NSG5GX8MNW=GS1.1.1661299672.1.1.1661299978.0.0.0; _ga=GA1.2.2020022182.1661299673; __stp={visit:new,uuid:dba12eaf-7e5b-48b7-b004-460e38776f1d}; __sts={sid:1661299672946,tx:1661299919580,url:https%3A%2F%2Fwww.guvi.com%2Fcode-kata-main%3Fconcept%3Darray,pet:1661299919580,set:1661299672946,pUrl:https%3A%2F%2Fwww.guvi.com%2Fcode-kata,pPet:1661299783098,pTx:1661299783098}; __stgeo=0; __stbpnenable=0; __stdf=0; _gid=GA1.2.942533324.1661299674; _fbp=fb.1.1661299674798.2071180317; _clck=pk5s33|1|f4a|0; _clsk=1glhtmh|1661299921034|6|1|b.clarity.ms/collect; G_ENABLED_IDPS=google; _cc_id=30ae4a31b9be802386a3bf8c78d08679; panoramaId_expiry=1661904537266; panoramaId=cd83b8c5d49866a0182dfa2604d716d53938c75bb29cded314f9e73ee60f3a60; USER_DATA=%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_USER_EMAIL%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%22gnspda%40gmail.com%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22b31c5cb1-2767-4d75-892d-2247e54422f1%22%2C%22deviceAdded%22%3Atrue%7D; moe_uuid=b31c5cb1-2767-4d75-892d-2247e54422f1; user_id=1183806; user_email=gnspda%40gmail.com; usertype=1; mp_74656ccf168534edf5fa89bedde46fb3_mixpanel=%7B%22distinct_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24device_id%22%3A%20%22182cd2e3d868c-040945ed48b8e6-c515424-19a100-182cd2e3d87b7c%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _gat_UA-53114947-1=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

        data = {
        'myData': '{"concept":"'+category+'","type":"qid","qid":'+str(completedQuestionID)+',"hash":"","authtoken":"02364c144fcdeabfe35e8168ffc8fb56cfc0b6bcdbf98170599d7df0a277d6cc7063e527d5fb5d1b53282efa3df647417041d68348a6a3a85dc9e2a2916e8228","originUrl":"www.guvi.com"}',
    }
        # print(data)
        response = requests.post('https://www.guvi.com/model/v2/codekata/codekataFetchQuestions.php', cookies=cookies, headers=headers, data=data)
        questionStatement = (json.loads(response.json()['questionData'])['question'])
        inputDesc = ""
        try:
            temp = (json.loads(response.json()['questionData'])['inputDescription']) + '\n'
            inputDesc = temp
        except:
            pass
        outputDesc = ""
        try:
            temp = (json.loads(response.json()['questionData'])['outputDescription']) + '\n'
            outputDesc = temp
        except:
            pass
        sampleInput = ""
        try:
            temp = 'Sample Input : \n' + (json.loads(response.json()['questionData'])['sampleInput']) + '\n'
            sampleInput = temp
        except:
            pass
        sampleOutput = ""
        try:
            temp = 'Sample Output : \n' + (json.loads(response.json()['questionData'])['sampleOutput']) + '\n'
            sampleOutput = temp
        except:
            pass
        qID =  (json.loads(response.json()['questionData'])['qid'])
        userCode = (json.loads(response.json()['questionData'])['submission']['sourceCode'])
        writeData = ('# QID: '+str(qID)+'\n') + ('\n' + questionStatement + '\n' + inputDesc + '\n' + outputDesc + '\n' + sampleInput + '\n' + sampleOutput).replace('<br>', '\n').replace('<p>','').replace('</p>', '').replace('&rsquo', '"').replace('&lsquo', '"').replace('&nbsp;', ' ').replace('<br />', '\n').replace('";', '').replace('&lt;', '<').replace('&gt;', '>').replace('Sample Testcase :', '\n\nSample Testcase :')
        # open(str(qID)+'.py', 'w').write(writeData)
        # print(response.json(), completedQuestionID)
        location = 'guvi/'+category+'/'
        if category == 'Input/Output':
            location = 'guvi/IO/'
        print(category, qID)
        try:
            open(location+str(qID)+'.py', 'w' , encoding="utf-8").write(writeData.replace('\n', '\n# '))
            open(location+str(qID)+'.py', 'a' , encoding="utf-8").write('\n\n\n# Solution:\n\n\n'+userCode)
        except:
            pass
        # break
    # break