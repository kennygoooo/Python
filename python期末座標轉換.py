import re
import speech_recognition as sr
import pyttsx3
from speech_recognition import UnknownValueError
import numpy as np
i=0
a=0
r = sr.Recognizer()
def speakText(command):
    print(command)
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
def AudioInput(i): #1:直角 2:極座標 3:圓球
    a=0
    if i == 1:
        while(a == 0):
            speakText("首先，請問X座標為多少？")
            Xsound = voiceReconize()
            regex = re.compile(r'(-*\d+)')
            try:
                match = regex.search(Xsound)
                X = match.group()
                X = float(X)
                a = 1
            except:
                speakText("偵測錯誤，請再說一次")
    while(a == 0):
        speakText("首先，請問r座標為多少？")
        Xsound = voiceReconize()
        regex = re.compile(r'(-*\d+)')
        try:
            match = regex.search(Xsound)
            X = match.group()
            X = float(X)
            a = 1
        except:
            speakText("偵測錯誤，請再說一次")
    if i == 1:
        while(a == 1):
            speakText("第二步，請問Y座標為多少？")
            Ysound = voiceReconize()
            regex = re.compile(r'(-*\d+)')
            try:
                match = regex.search(Ysound)
                Y = match.group()
                Y = float(Y)
                a = 2
            except:
                speakText("偵測錯誤，請再說一次")
    while(a == 1):
            speakText("第二步，請問極角為多少？")
            Ysound = voiceReconize()
            regex = re.compile(r'(-*\d+)')
            try:
                match = regex.search(Ysound)
                Y = match.group()
                Y = float(Y)
                a = 2
            except:
                speakText("偵測錯誤，請再說一次")
    if i == 3:
        while(a == 2):
            speakText("快成功了！請問方位角為多少？")
            Zsound = voiceReconize()
            regex = re.compile(r'(-*\d+)')
            try:
                match = regex.search(Zsound)
                Z = match.group()
                Z = float(Z)
                a = 3
            except:
                speakText("偵測錯誤，請再說一次")
    while(a == 2):
        speakText("快成功了！請問Z座標為多少？")
        Zsound = voiceReconize()
        regex = re.compile(r'(-*\d+)')
        try:
            match = regex.search(Zsound)
            Z = match.group()
            Z = float(Z)
            a = 3
        except:
            speakText("偵測錯誤，請再說一次")
    return X,Y,Z

def voiceReconize():
    try:
        audio2 = r.listen(source2)
        s = r.recognize_google(audio2, language='zh-TW')
        print(s)
        return s
    except UnknownValueError:
        pass
def CartesianToCylindrical(): #直角座標轉圓柱坐標
    X,Y,Z = AudioInput(1)

    x_square = np.square(X)
    y_square = np.square(Y)
    r = x_square + y_square
    R = np.sqrt(r)
    Q = np.arctan2(Y,X)*180/np.pi
    print("(r,φ,Z) = ",'(',round(R,2),round(Q,2),round(Z,2),')')
    speakText('恭喜！你得到的r座標是'+str(round(R,2))+'，極角是'+str(round(Q,2))+'度'+'，Z座標是'+str(round(Z,2)))


def CartesianToSpherical(): #直角坐標轉球座標
    X,Y,Z = AudioInput(1)
    
    x_square = np.square(X)
    y_square = np.square(Y)
    z_square = np.square(Z)
    r = x_square + y_square + z_square
    R = np.sqrt(r)
    P = np.arccos(Z/r)
    Q = np.arctan2(Y,X)*180/np.pi
    print("(R,θ,φ) = ",'(',round(R,2),round(P,2),round(Q,2),')')
    speakText('恭喜！你得到的R座標是'+str(round(R,2))+'，極角是'+str(round(P,2))+'度'+'，方位角是'+str(round(Q,2))+'度')

def CylindricalToCartesian(): #圓柱座標轉直角座標
    length,angle,Z = AudioInput(2)
    
    sin = np.sin(np.deg2rad(angle))#角度轉弧度
    Y = length*sin
    cos = np.cos(np.deg2rad(angle))#角度轉弧度
    X = length*cos
    print("(X,Y,Z) = ",'(',round(X,2),round(Y,2),Z,')')#四捨五入取小數後第二位
    speakText("恭喜！你得到的X座標是:"+str(round(X,2))+"，Y座標是:"+str(round(Y,2))+"，Z座標是:"+str(round(Z,2)))

def CylindricalToSpherical(): #圓柱座標轉球座標
    length,angle,Z = AudioInput(2)
    
    x_square = np.square(length)
    z_square = np.square(Z)
    
    R = np.sqrt(x_square + z_square)
    Q = np.arctan2(R,Z)*180/np.pi
    
    print("(R,θ,φ) = ",'(',round(R,2),round(angle,2),Q,')')#四捨五入取小數後第二位
    speakText("恭喜！你得到的R座標是:"+str(round(R,2))+"，極角是:"+str(round(angle,2))+'度'+"，方位角是:"+str(round(Q,2))+'度')

def SphericalToCartesian(): #球座標轉直角座標
    R,angle1,angle2 = AudioInput(3)
    
    X = R*np.sin(np.deg2rad(angle1))*np.cos(np.deg2rad(angle2))
    Y = R*np.sin(np.deg2rad(angle1))*np.sin(np.deg2rad(angle2))
    Z = R*np.cos(np.deg2rad(angle1))
    
    
    print("(X,Y,Z) = ",'(',round(X,2),round(Y,2),Z,')')#四捨五入取小數後第二位
    speakText("你得到的X座標是:"+str(round(X,2))+"，Y座標是:"+str(round(Y,2))+"，Z座標是:"+str(round(Z,2)))
def SphericalToCylindrical(): #球座標轉圓柱座標
    R,angle1,angle2 = AudioInput(3)
    
    r = R*np.sin(np.deg2rad(angle1))
    Z = R*np.cos(np.deg2rad(angle1))
    
    print("(r,φ,Z) = ",'(',round(r,2),round(angle1,2),round(Z,2),')')#四捨五入取小數後第二位
    speakText("你得到的r座標是:"+str(round(r,2))+"，極角是:"+str(round(angle1,2))+'度'+"，Z座標是:"+str(round(Z,2)))
def ResponceCheck(a):
    try:
        myResponse = voiceReconize()
        if '不' not in myResponse:
            a = 1
        else:
            speakText('重新判斷 請再說一次')
            a=0#此錯誤可能是沒偵測到聲音 或 使用者說不是
    except TypeError:
        speakText('重新判斷 請再說一次')
        a=0
    return a
    
with sr.Microphone() as source2:
    speakText("本計算機提供直角座標、極座標、球座標之座標值轉換，如不是做座標轉換，請關閉程式去找其他計算機，謝謝")
    speakText("偵測雜音中")
    r.adjust_for_ambient_noise(source2, duration=2)
    speakText("偵測雜音完畢，請問要什麼轉什麼？")
    while(a==0):
        myText = voiceReconize()
        
        p = re.compile(r'.*([机极極急直職球]).*[转轉]([机极極急直職球]).*')
        try:
            m = p.match(myText)
        except TypeError:
            m = False
        if m:
            
            if m.group(1) in ('直','職') and m.group(1)!=m.group(2) :
                i = 1 if m.group(2) in ('極','急','极','机') else 2
                speakText('請問是直角座標轉極座標嗎？') if i == 1 else speakText('請問是直角座標轉球座標嗎？')
                a = ResponceCheck(a)
            elif m.group(1) in ('極','急','极','机') and m.group(1)!=m.group(2):
                i = 3 if m.group(2) in ('直','職') else 4
                speakText('請問是極座標轉直角座標嗎？') if i == 3 else speakText('請問是極座標轉球座標嗎？')
                a = ResponceCheck(a)
            elif m.group(1)=='球' and m.group(1)!=m.group(2):
                i = 5 if m.group(2) in ('直','職') else 6
                speakText('請問是球座標轉直角座標嗎？') if i == 5 else speakText('請問是球座標轉極座標嗎？')
                a = ResponceCheck(a)
        else:
            speakText('聽不懂 再說一次') #此錯誤可能是沒偵測到聲音 或 被轉換座標與轉換座標相同
    if i == 1:
        CartesianToCylindrical()
    elif i == 2:
        CartesianToSpherical()
    elif i == 3:
        CylindricalToCartesian()
    elif i == 4:
        CylindricalToSpherical()
    elif i == 5:
        SphericalToCartesian()
    else:
        SphericalToCylindrical()
    speakText('感謝您此次使用本計算機，歡迎下次再使用我，啾咪')