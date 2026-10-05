from loja.models import *

class Favorito(models.Model):
    user = models.ForeignKey(User, related_name='favoritos', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='favoritos', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    class Meta:
        # um usuário só pode favoritar o mesmo produto uma vez
        unique_together = ('user', 'produto')
    def __str__(self):
        return '{} - {}'.format(self.user.username, self.produto)