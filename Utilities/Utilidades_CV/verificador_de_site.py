import requests


def situação_site(link="Digite o link do site: "):
    try:
        url = input(link).strip()
        requests.head(url)
    except(TypeError, ValueError):
        return "\033[0;31mERRO! Por favor, digite um link válido.\033[m "
    except KeyboardInterrupt:
        return "\n\033[0;31mO usuário preferiu não digitar esse link.\033[m "
    except:
        return "\033[0;33mSite não está disponível no momento! Tente novamente mais tarde.\033[m "
    else:
        return "\033[0;32mSite está disponível!\033[m "