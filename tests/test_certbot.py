def test_certbot_cli(Command):
    assert Command('letsencrypt --version').rc == 0
