citys = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA' , 'SP', 'MG', 'RJ'] 

def zipper(citys, states):

    intervalo = min (len(citys), len(states))
    return [
         (citys[i], states[i]) for i in range (intervalo)
     ]



print(zipper(citys, states))