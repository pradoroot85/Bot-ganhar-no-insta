from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time 


def fazerTarefa():
    print('')
    print('BOT ONLINE...')
    print('')
    bot = webdriver.Chrome('./chromedriver')
    print('LOGANDO NO INSTAGRAM...')
    bot.get('https://www.instagram.com/')
    time.sleep(3)
    email = bot.find_element_by_name('username')
    email.send_keys('SEU EMAIL')
    senha = bot.find_element_by_name('password')
    senha.send_keys('SUA SENHA', Keys.ENTER)
    time.sleep(5)
    print('LOGIN NO GANHAR NO INSTA...')
    bot.get('https://www.ganharnoinsta.com/painel/?pagina=logout')
    email1 = bot.find_element_by_id('uname')
    email1.send_keys('SEU EMAIL')
    senha1 = bot.find_element_by_id('pwd')
    senha1.send_keys('SUA SENHA', Keys.ENTER)
    time.sleep(5)
    print('')
    print('INICIAR TAREFAS....')
    print('')
    bot.get('https://www.ganharnoinsta.com/painel/?pagina=sistema')
    time.sleep(5)
    bot.find_element_by_id('btn_iniciar').click()
    time.sleep(5)
    
    while True:
        while len(bot.find_elements_by_id('btn-acessar'))<1:
            time.sleep(1)
            print('')
            print('ESPERANDO...')
            print('')
        bot.find_element_by_id('btn-acessar').click()
        print('')
        print('OLHANDO QUEM EU VOU SEGUIR...')
        print('')
        time.sleep(5)
        bot.switch_to.window(bot.window_handles[-1])
        time.sleep(5)
        print('')
        print('SEGUINDO')
        print('')
        bot.find_element_by_class_name('_7UhW9.xLCgt.qyrsm.uL8Hv.T0kll').click()
        bot.close()  
        print('FECHAR JANELA')
        bot.switch_to.window(bot.window_handles[-1])
        time.sleep(2)
        bot.find_element_by_id('btn-confirmar').click()
        print('')
        print('CONFIRMEI A TAREFA E VOU REPETIR!')
        print('')
