"""
Testes básicos para o sistema CRUD
Execute com: python tests.py
"""

import Backend as core
import os


def limpar_banco_teste():
    """Remove banco de teste se existir"""
    if os.path.exists("clientes.db"):
        os.remove("clientes.db")
    print("🧹 Banco de teste limpo")


def test_insert():
    """Testa inserção de cliente"""
    print("\n📝 Testando inserção...")
    core.initDB()
    core.insert("João", "Silva", "joao@email.com", "12345678901")
    rows = core.view()

    assert len(rows) > 0, "Erro: Nenhum registro inserido"
    assert rows[0][1] == "João", "Erro: Nome incorreto"
    print("✅ Teste de inserção passou!")


def test_view():
    """Testa visualização de todos os clientes"""
    print("\n👀 Testando visualização...")
    rows = core.view()

    assert len(rows) > 0, "Erro: Nenhum registro encontrado"
    print(f"✅ Teste de visualização passou! ({len(rows)} registros)")


def test_search():
    """Testa busca por nome"""
    print("\n🔍 Testando busca...")
    rows = core.search(nome="João")

    assert len(rows) > 0, "Erro: Busca não retornou resultados"
    assert "João" in rows[0][1], "Erro: Nome não encontrado"
    print("✅ Teste de busca passou!")


def test_update():
    """Testa atualização de cliente"""
    print("\n✏️ Testando atualização...")
    rows = core.view()
    id_primeiro = rows[0][0]

    core.update(id_primeiro, "Maria", "Santos", "maria@email.com", "98765432100")
    rows_atualizadas = core.view()

    assert rows_atualizadas[0][1] == "Maria", "Erro: Atualização falhou"
    print("✅ Teste de atualização passou!")


def test_delete():
    """Testa exclusão de cliente"""
    print("\n🗑️ Testando exclusão...")
    rows_antes = core.view()
    qtd_antes = len(rows_antes)

    id_deletar = rows_antes[0][0]
    core.delete(id_deletar)

    rows_depois = core.view()
    qtd_depois = len(rows_depois)

    assert qtd_depois == qtd_antes - 1, "Erro: Exclusão falhou"
    print("✅ Teste de exclusão passou!")


def executar_todos_testes():
    """Executa todos os testes em sequência"""
    print("=" * 50)
    print("🧪 INICIANDO TESTES DO SISTEMA CRUD")
    print("=" * 50)

    try:
        limpar_banco_teste()
        test_insert()
        test_view()
        test_search()
        test_update()
        test_delete()

        print("\n" + "=" * 50)
        print("🎉 TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("=" * 50)

    except AssertionError as e:
        print(f"\n❌ TESTE FALHOU: {e}")
    except Exception as e:
        print(f"\n💥 ERRO INESPERADO: {e}")
    finally:
        print("\n🧹 Limpando banco de teste...")
        limpar_banco_teste()


if __name__ == "__main__":
    executar_todos_testes()