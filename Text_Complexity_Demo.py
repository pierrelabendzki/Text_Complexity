import pylzma
from pylzma import compress
import string    
import random # define the random module  
import numpy as np
from scipy.io import wavfile as io
import matplotlib.pyplot as plt 

import plotly 
import plotly.express as px
import plotly.io as pio
import plotly.graph_objs as go


def id_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.whitespace + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


def com(string):
    compressed = pylzma.compress(string, eos = 0)
    return len(compressed)


def comp(string):
    print('len string',len(string))
    reduce = com(str(np.zeros(len(string))))
    print('reduce',reduce)
    compressed = pylzma.compress(string, eos = 0)
    print('len compression',len(compressed))
    print('finale score',(len(compressed)-reduce)/len(string)-reduce)
    return((len(compressed)-reduce)/len(string))


def Kolmo(string):
    reduce = com("a" * len(string))
    # print('reduce',reduce)
    compressed = pylzma.compress(string, eos = 0)
    return (len(compressed)-reduce)

def Kolmo_conditional(string, memory):
    Kds = Kolmo(memory+' '+string)
    Kd = Kolmo(memory)
    # print('Kolmo conditional : ')
    return Kds - Kd


def Distance(a,b):
    d = min(Kolmo_conditional(a,b),Kolmo_conditional(b,a))
    # print('Distance : ')
    return d

def derivative(x):
    step = 5
    out = np.zeros(len(x)-step+1)
    for k in range(step,len(x)-(step+1)):
        temp_sum = 0
        for i in range(step-1):
            temp_sum = temp_sum + (x[k+step-i] - x[k-step+i])
        out[k] = temp_sum   
    return out

def complexity_cumul(string):
    N = len(string)
    results = np.zeros(N)
    for k in range(N):
        results[k]= Kolmo(string[0:k+1])
    return results  

def complexity_sliding(string,ws):
    N = len(string)
    results = np.zeros(N)
    for k in range(N):
        if (k<ws):
            results[k]= Kolmo(string[0:ws])
        if (k>N+ws):
            results[k]= Kolmo(string[N-ws:N])
        if((k>ws) and (k<N-ws)):
            results[k]= Kolmo(string[k-ws:k+ws])
    return results

rando = id_generator(1000)
baby_shark = 'Baby shark, doo doo doo doo doo doo Baby shark, doo doo doo doo doo doo Baby shark, doo doo doo doo doo doo Baby shark! Mommy shark, doo doo doo doo doo doo Mommy shark, doo doo doo doo doo doo Mommy shark, doo doo doo doo doo doo Mommy shark!  Daddy shark, doo doo doo doo doo doo Daddy shark, doo doo doo doo doo doo Daddy shark, doo doo doo doo doo doo Daddy shark! Grandma shark, doo doo doo doo doo doo Grandma shark, doo doo doo doo doo doo Grandma shark, doo doo doo doo doo doo Grandma shark! Grandpa shark, doo doo doo doo doo doo Grandpa shark, doo doo doo doo doo doo Grandpa shark, doo doo doo doo doo doo Grandpa shark! Let’s go hunt, doo doo doo doo doo doo Let’s go hunt, doo doo doo doo doo doo Let’s go hunt, doo doo doo doo doo doo Let’s go hunt!'
super_freak = 'She’s alright (She’s alright, that girl’s alright) That girl’s alright with me Yeah   Ay, yo   I can lick it, I can ride it While you slippin and sliding I can do all them little tricks and keep the dick up inside it You can smack it, you can grip it You can go down and kiss it And every time he leave me lone he always tell me he miss it He want a F-R-EEEEE-A-K F-R-EEEEE-A-K, A-K, A-K, A-K EEEEE-A-K, F-R-EEEEE-A-K   Ok, one thing about me, I’m the baddest alive He know the prettiest bitch didn’t come until I ARRIVE I don’t let bitches get to me; I fuck they man if they try I got a princess face, a killer body, samurai mind They can’t be Nicki, they so stupid, I just laugh when they try A thong bikini up my ass, I think I’ll go for a dive His ex bitch went up against me, but she didn’t survive On applications I write pressure, ‘cause that’s what I apply (Brrrr) P P P Pressure applied, can’t fuck a regular guy Wetter than umbrellas and stickier than Apple Pie   I can lick it, I can ride it While you slipping and sliding I can do all them little tricks and keep the dick up inside it You can smack it, you can grip it You can go down and kiss it And every time he leave me ‘lone he always tell me he miss it He want a F-R-EEEEE-A-K F-R-EEEEE-A-K, A-K, A-K, A-K EEEEE-A-K, F-R-EEEEE-A-K   ‘Cause what the fuck, this ain’t Chanel, nigga, custom down? Like, what the fuck, this ain’t Burberry, custom brown? He said, “Could you throw it back while you touch the ground?” Then he said, “Do that pussy purr?” I said, “Yup, meow” Hold up Fuck boys, ain’t no need for you to roll up Ain’t no need for you to double tap neither, scroll up Keep these bitches on they toes like Manolo Be on the lookout when I come through, BOLO Oh, whoa  Elegant  bitch with a  hoe glow If it ain’t big, then I won’t blow Eeny, meeny, miny, moe Fuck is the tea? I just F’d a G Made him say “Uhh”, just ask Master P Ball so hard, I just took a knee Get me Rocky A$AP, nigga, word to RIH   Freak F-f-freak Some GYAL A FREAK GYAL AH  FREAK GYAL AH freak, freak, freak   I can lick it, I can ride it While you slipping and sliding  I can do all them little tricks and keep the dick up inside it You can smack it, you can grip it You can go down and kiss it And every time he leave me ‘lone he always tell me he miss it He want a F-R-EEEEE-A-K F-R-EEEEE-A-K, A-K, A-K, A-K EEEEE-A-K, F-R-EEEEE-A-K'
fox_and_crow = 'Sensory regulation, the ability to select and process sensory information to plan and perform appropriate behaviours, provides a foundation for learning. From early in development, infants manifest differences in the strategies used for sensory regulation. Here, we discuss the nature and characteristics of sensory seeking, a key behavioural strategy for sensory regulation often described as atypical in children with Neurodevelopmental Disorders. We evaluate theoretical models proposed to clarify mechanisms underlying individual differences in sensory seeking and discuss evidence for/against each of these models. We conclude by arguing that the information prioritization hypothesis holds the greatest promise to illuminate the nature of individual differences in sensory seeking across participant cohorts. This proposal aligns to molecular genetic animal and human evidence, provides a coherent explanation for developmental findings, and generates testable hypotheses for future research. The temporal structure of behavior contains a rich source of information about its dynamic organization, origins, and development. Today, advances in sensing and data storage allow researchers to collect multiple dimensions of behavioral data at a fine temporal scale both in and out of the laboratory, leading to the curation of massive multimodal corpora of behavior. However, along with these new opportunities come new challenges. Theories are often underspecified as to the exact nature of these unfolding interactions, and psychologists have limited ready-to-use methods and training for quantifying structures and patterns in behavioral time series. In this paper, we will introduce four techniques to interpret and analyze high-density multi-modal behavior data, namely, to: (1) visualize the raw time series, (2) describe the overall distributional structure of temporal events (Burstiness calculation), (3) characterize the non-linear dynamics over multiple timescales with Chromatic and Anisotropic Cross-Recurrence Quantification Analysis (CRQA), (4) and quantify the directional relations among a set of interdependent multimodal behavioral variables with Granger Causality. Each technique is introduced in a module with conceptual background, sample data drawn from empirical studies and ready-to-use Matlab scripts. The code modules showcase each technique’s application with detailed documentation to allow more advanced users to adapt them to their own datasets. Additionally, to make our modules more accessible to beginner programmers, we provide a “Programming Basics” module that introduces common functions for working with behavioral timeseries data in Matlab.'

print('\n Computing Compression Ratios... \n')
print('redundancy of random : ',Kolmo(rando)/len(rando))
print('redundancy of baby_shark : ',Kolmo(baby_shark)/len(baby_shark))
print('redundancy of super_freak : ',Kolmo(super_freak)/len(super_freak))
print('redundancy of fox_and_crow : ',Kolmo(fox_and_crow)/len(fox_and_crow))



### Computing the cumulative (integrative) windows
### For text that are 5000 characters long, this can a minute
print('\n Computing cumulative windows... \n')
cumul_rando = complexity_cumul(rando)
cumul_CDSo = complexity_cumul(baby_shark)
cumul_ADSo = complexity_cumul(super_freak)
cumul_CDSt = complexity_cumul(fox_and_crow)


### Computing the cumulative (integrative) windows
print('\n Computing derivatives... \n')
deriv_rando = derivative(cumul_rando)
deriv_CDSo = derivative(cumul_CDSo)
deriv_ADSo = derivative(cumul_ADSo)
deriv_CDSt = derivative(cumul_CDSt)



### PLotting results of the cumulative window
plt.subplot(2,1,1)
plt.title('Texts complexity - cumulative and derivative analysis')
plt.plot(cumul_rando,label = 'Random')
plt.plot(cumul_CDSo,label = 'CDSo')
plt.plot(cumul_ADSo,label = 'ADSo')
plt.plot(cumul_CDSt,label = 'CDSt')

plt.xlabel('size of the integrative window of analysis')
plt.ylabel('compressed size')
plt.legend()


### Plotting the results of the derivative
plt.subplot(2,1,2)
plt.plot(deriv_rando,label = 'Random')
plt.plot(deriv_CDSo,label = 'CDSo')
plt.plot(deriv_ADSo,label = 'ADSo')
plt.plot(deriv_CDSt,label = 'CDSt')

plt.xlabel('size of the integrative window of analysis')
plt.ylabel('derivative of compressed size')
plt.legend()

plt.show()


