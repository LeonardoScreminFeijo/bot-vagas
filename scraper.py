from playwright.sync_api import sync_playwright
import time

def testar_extracao():
    print('Iniciando busca...')
    
    with sync_playwright() as p:
        browser=p.chromium.launch()
        page = browser.new_page()

        url_busca = "https://www.linkedin.com/jobs/search/?currentJobId=4376403848&f_WT=2&geoId=106057199&keywords=Engenheiro%20De%20Software&location=Brasil&originalSubdomain=br"

        print("Acessando Linkedin")
        page.goto(url_busca)

        page.wait_for_timeout(3000)

        print("Extraindo as primeiras vagas...")
        cards_vagas = page.locator("ul.jobs-search__results-list > li").all()

        if not cards_vagas:
            print("Nenhuma vaga encontrada ou layout mudou")

        for vaga in cards_vagas:
            try:
                titulo = vaga.locator("h3").inner_text().strip()
                empresa = vaga.locator("h4").inner_text().strip()
                link = vaga.locator("a").first.get_attribute("href").split("?")[0]

                print(f'Cargo: {titulo}')
                print(f'Empresa: {empresa}')
                print(f'Link: {link}')
                print("-" * 50)
            except Exception as e:
                print("Erro ao ler um card de vaga:", e)

                print("\n✅ Teste concluído. Fechando o navegador em 5 segundos...")
        time.sleep(5)
        browser.close()

if __name__ == "__main__":
    testar_extracao()