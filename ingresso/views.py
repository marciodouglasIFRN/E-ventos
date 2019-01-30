from django.http import HttpResponse
from django.views.generic import CreateView, ListView, View, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from clientes.models import Aluno
from evento.form import EventoForm
from evento.models import Evento
from ingresso.form import IngressoForm
from ingresso.form import IngressoNewEvento
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from .models import Ingresso
import io
import qrcode
import random


def erro_Permissao1(request):
    return render(request, "evento/sempermissao.html")

@permission_required('ingresso.add_ingresso', login_url='erro_permissao1')
def solicitarIngressoFuncao(request, id_evento):
    form = IngressoNewEvento(request.POST or None)
    evento = get_object_or_404(Evento, pk=id_evento)
    chave = evento.pk
    formEvento = EventoForm(request.GET or None, instance=evento)
    if form.is_valid() and int(evento.quantidaIngresso) > 0:
        evento.quantidaIngresso = int(evento.quantidaIngresso) - 1
        evento.save()
        ran1 = random.randint(0, 9999999999999)
        caminho = 'statics/qrcode/img_' + str(ran1) + '_qrcode.png'
        # ins = form.save(commit=False)
        ins = form.save()
        ins.caminho = caminho
        ins.save()
        gerarQrCode(evento, caminho)
        #gerarQrCode(evento, form)
        return redirect('page-home')

    return render(request, 'ingresso_form_funcao.html', {'formIngresso':form,'formEvento': formEvento, 'chaveForm': chave})



@permission_required('ingresso.delete_ingresso', login_url='erro_permissao1')
def cancelarSolicitacaoFuncao(request, id_ingresso, id_evento):
    ingresso = get_object_or_404(Ingresso, pk=id_ingresso)
    evento = get_object_or_404(Evento, pk=id_evento)
    if request.method == 'POST':
        evento.quantidaIngresso = int(evento.quantidaIngresso)+1
        evento.save()
        ingresso.delete()
        return redirect('minhas_solicitacoes')
    return render(request, 'ingresso_delete_confirm.html', {'ingresso': ingresso})


class MinhasSolicitacoes(ListView):
    model = Ingresso
    def get_queryset(self):
        return Ingresso.objects.filter(aluno=self.request.user.pessoa.aluno.pk)

def autenticarIngresso(request, id_aluno, id_evento, id_ingresso):
    aluno = get_object_or_404(Aluno, pk=id_aluno)
    evento = get_object_or_404(Evento, pk=id_evento)
    ingresso = get_object_or_404(Ingresso, pk=id_ingresso)
    if request.method == 'GET':
        return render(request, 'ingresso/autenticar.html', {'evento': evento, 'aluno':aluno, 'ingresso':ingresso})

class SolicitarIngresso(CreateView):
    model = Ingresso

    form_class = IngressoForm

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(SolicitarIngresso, self).get_form_kwargs()
        kwargs.update({"evento": self.kwargs['pk']})
        return kwargs

    success_url = 'page-home'



class Render:
    
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):

    def get(self, request, **kwargs):
        ingre = get_object_or_404(Ingresso,pk=kwargs['id_ingresso'])
        #chave = ingre.pk
        chave =  ingre
        #evento = get_object_or_404(Evento, pk=ingre.evento)
        
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
            'ingresso':chave,
        }
        return Render.render('ingresso/modeloIngresso.html', params, 'myFile')

def gerarQrCode(id_evento, caminho):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('Codigo do ingresso:' + str(id_evento.pk) + '. Nome da Atração:')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", black_color="white")
    img.save(caminho)
    