import utils.mail


def confirmerInscription(formEquipe):
    equipe = formEquipe.cleaned_data['nomEquipe']
    categorie = formEquipe.cleaned_data['categorie']

    subject = "Inscription Coupe MGENI"
    message = """
    <div style="height:25px;">
    </div>

    <p>
        Merci d’avoir procédé à l’inscription du votre équipe au tournoi Futsal Association Centre Vi-Foot avec l'équipe <strong>{nom_equipe}</strong> dans la categorie <strong>{categorie}</strong>.
    </p>
    <p>
         Il nous fera plaisir de vous accueillir les 23 et 24 mars à l’école Rochebelle.
    </p>
    <p>
        Votre inscription sera officielle lors de la réception de votre chèque au montant de 180$, au nom de « Association Centre Vi-Foot ».
    </p>
    <p>
        Merci de transmettre votre chèque à l’adresse suivante :
    </p>
    <div style="width:200px;">
        <div>
            <div style="float: left;padding-left:25px;width:100%;">677 ave de Norvège, local 3</div>
            <div style="float: left;padding-left:25px;width:100%;">Québec, Qc</div>
            <div style="float: left;padding-left:25px;width:100%;">G1X 3G5</div>
        </div>
    </div>

    <div style="height:100px;">
    </div>

    <div style="color:#666699;">
        <div style="float: left;width:100%;">______________________________________________</div>
        <h2 style="float: left;width:100%;margin-bottom:0px;">Janick Houle</h2>
        <a style="float: left;width:100%;font-style: italic;">Directeur du soutien aux opérations</style>
        <a style="float: left;width:100%;" href="mailto:janick.houle@vi-foot.com" target="_top">janick.houle@vi-foot.com</a>
        <div style="float: left;width:100%;font-size:20px;">Centre De Formation Vi-Foot</div>
        <div style="float: left;width:100%;">677 avenue Norvège Local: 3</div>
        <div style="float: left;width:100%;">Ville de Québec, Qc G1X 3G5</div>
        <div style="float: left;width:100%;">Tél: 1(581)998-8808</div>
        <a style="float: left;width:100%;" href="mailto:info@vi-foot.com" target="_top">info@vi-foot.com</a>
        <a style="float: left;width:100%;" href="www.vi-foot.com" target="_top">www.vi-foot.com</a>
    </div>

    """.format(nom_equipe=equipe, categorie=categorie)
    #message = """Bonjour, \n vous etes inscrits pour le tournoi avec l'equipe {nom_equipe} dans la categorie {categorie}""".format(nom_equipe=equipe, categorie=categorie)
    sender = "janick.houle@vi-foot.com"
    to = [formEquipe.cleaned_data['emailContact'], "shadrack.mmunga@vi-foot.com"]
    #utils.mail.envoi_de_mail(subject,message,sender,to)
