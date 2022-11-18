import unittest

def testa(largura, comprimento, historico):
    cartografia = { 90: "O",  180 : "N" , 270 : "L",  0: "S"} #Pega o modulo da posição por 360° e intentifica a orientação do robô
    posicao = 180 #Começa na posição Norte (Considerei 180° como norte e 360° como sul)
    coordX = 0 
    coordY = 0
    for i in range(len(historico)):
        if historico[i]=='D': #Como é no sentido horário, quando vira para direita soma 90
            posicao += 90
        if historico[i] == 'E': #Como é no sentido anti-horário, quando vira para esquerda diminui 90
            posicao -= 90
        if historico[i] == 'F': #Como vai andar pra frente, aumenta 1 no sentido que está o robô; Fazendo com que ou some ou diminua 1 na coordenada
            if cartografia[posicao%360] == "N" and (coordY+1) < comprimento: #verifica se somando 1 ainda será menor q o comprimento, igual nas de mais
                coordY += 1
            if cartografia[posicao%360] == "S" and (coordY-1) >= 0.0: # verifica se diminuindo 1 ainda será maior ou igual a zero, igual nas de mais
                coordY -= 1
            if cartografia[posicao%360] == "L" and (coordX+1) < largura:
                coordX += 1
            if cartografia[posicao%360] == "O" and (coordX-1) >= 0.0:
                coordX -= 1
        if historico[i] == 'T': #Como vai andar pra trás, faz o exato inverso de quando anda pra frente, pois está na mesma direção, mas anda no sentido inverso
            if cartografia[posicao%360] == "N" and (coordY-1) >= 0.0:
                coordY -= 1
            if cartografia[posicao%360] == "S" and (coordY+1) < comprimento:
                coordY += 1
            if cartografia[posicao%360] == "L" and (coordX-1) >= 0.0:
                coordX -= 1
            if cartografia[posicao%360] == "O" and (coordX+1) < largura:
                coordX += 1
    return f'{cartografia[posicao%360]} {coordX} {coordY}'

class MyTest(unittest.TestCase): #Casos de teste de acordo com o enunciado
    def test(self):
        self.assertEqual((testa(10, 10, 'FFFFFFFFFDFFFFFFFFFDFFFFFFFFFDFFFFFFFFF')), 'O 0 0')
    def test2(self):
        self.assertEqual((testa(5, 5, 'FDFEFDFEFDFEFDF')), 'L 4 4')
    def test3(self):
        self.assertEqual((testa(1232, 1232, 'TTTTTTTTTTTTT')), 'N 0 0')
    def test4(self):
        self.assertEqual((testa(15, 36, 'FFFFFFFFFFFFFFFFDFETTTTTTTTTTTTTTTT')), 'N 1 0')
    def test5(self):
        self.assertEqual((testa(50, 50, 'TTFFDTTETDEDTTDDFFDEFDTEFTTDDEDEFFTEETEDTTEEDDEFFFTEDFDFTTDDDTTTTTFDEFDFFTEDTEDEFTDTETETFDFTDTFEFDTFTTEEFEEFEDDTFTEDFFTTDTTTFDETETDDTEDDTFEDFDEFDDTTDEFEFTDTTDFFEDDTDFDETTDDFFTEEDFFTTTDETFTFDTETTTTDEFFETFTDFDTEEDFTEFTEFFFTDEEDDTTEFDFETDFEEETTDFTTTEEEEEDTETFETTETDEEFTTDDDFFTFDDEFDEFTTTEDFFFTEEDTDDTTDFDEETTDETETDDETTTDEFEETTETDEDTEFTTDDEEFDFDTEEEDEDTDDTEEEEEDTFEDEDDDTTTFFDETFFDDTFDTEFFFDDFEEFEFDDFDTTETTDTDTTTDEDFTTDDDTTTTTDTEDFEFDTFFETEEEFFFEFDTTDETTFFETTDEETFEDTEFFDEEFEEDTTFFTEEETDTEEEFTFFEFEFDFFEFTFEDEEDFDDDFDFEFEDDDTEETTETFTTFDTDEFTFEEDEFTEFETFEEEFDETEDFFTFDFFTFDTFEFDEDTTTFEDEFTTDDEEFDTFTEEDTETEFEFFEEEFFTFEETEDDFFFTFDETFDEFETDTFDDFFTFDTFTTFTTFDFDDEDEFFFETTTTFFFFTDEEEFTDFDDFTFETDDEDFFFEFFDDDTTDEFETFDEFDEDETDFEETEDTFETTTFEEEFTETFFTDFDFEDFTDDTEFTFFEFEEFTTTFEEFTDDDEEDTFTFDTTDFDEETFFTDFDEDEEFFDTFETEDEETTEFFFDETTTFTEETFDTEFFEEFFDEDFFDTTEFDETDDETDDDTDFETTTETEEEFDFTEETDTEDETTEDETFEEEFTFFEEDTFFFTEDDFDDFDDTTEDEETETEEFDDDTTTTTEEFEFFFTEFEDEFEFEFEDDFFEEEFEETTFDFEEDDTTTTETDTEDEFFDFTTFFTDTEDEDEDDFEFT')), 'S 11 13')
    def test6(self):      
        self.assertEqual((testa(1000, 1000, 'EDFFEDFTTEDFTETEFDTFDTDTDTFDFTDEDTFFTFTDDDETFTFEFETEFEEEDFTTEFEEDFTFFTFTDTTDFDDDTFTTTDDEETDDFTDFFETTDTTTFEEFFTDTFETDEFEDEFDFDTTEFDEEDTTDDETTDEDTTEEEFFEEDDDETDFDTEDEDFTFFEEDEDDFEDEDFDDFEDEETTFTETFTTTEETTFDDTTEFDDEDTDEDEDDFTFEFTDFEFFDTETFFFTDTFTEFFFEDETFETTFETDFFFDEETETFEFFTFETFEFFTEETDETDEFEFTFDEEFDEEDTEDEFEFTEETTTTFEEFTDTDDFDEDFEDDDDTEDDDTFDDDEEEEDTTDFEDTDETFTFTFDFTFTDFEDEFDEEEDDETEEEDDTEFEFFFDTEFTFFEETETEDDDDEFTEEDDEDDTTDTTEDFEFETFTDTFTFEEDEFEDTEFDEEDEDEFDTEDEETEDEDEDDEDTDTDDFFEFDEETTEDDEFFTFDEFEFFDFDDTFEFTTDDDTDTDDFDEEDETDDDFEFTEDEFEEFDETEFTDFTFDDFTFEEDEEEEEDDDTEDDFTDFDFFFDTETTTDETTEDETEDDETETDEEFTTFTDDFDEEEFFDEDTEDFTEETTEFDDFTFEFEEEETFTEFTEDFTFFEEEDFDETTEFDTFFDDDFFDTEEFETDTETFDFTDEDTFFFFEETTFDFDDFTDTTDFFTFDDDTDTDDFDDEETETTFETTEFDTTFEDDFDTEDETTTEDTDEFFEFFFTDTEDTTTEFFTTTTDFTDFTETDDFDEEFEFTEFTTDDDTEFEFETDDDDTETTTETEEDEETTDDFTDTETTFTFFTEFFEEDEEEFTTDEEEEFEDTEEEDEEDDDTETEFEFDDDEDEFEFTTDFDTTDEDFTFDDTDTFDDDDEFEEEDEDDTTTDDTEDTEDDTDTDDTFETDTDTDFDDDTTEEEFEDTEFFDEEDTTEFTDEDTDDETEFEFEFFTTTEEFDEF')), 'L 25 5')

    
if __name__ == '__main__': #Chama classe de teste
    unittest.main()
