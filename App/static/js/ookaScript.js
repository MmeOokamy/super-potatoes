// Variable pour la tableau de la recherche des préférences
var ventilations = [];

// Paramétrage des options FuzzySort
var searchOptions = {
   threshold: -1000, // Pour ne pas retourner les mauvais résultats
   limit: 20, // Nombre de résultats max
   allowTypo: true, // On autorise une faute
   key: "label", // On dit sur quel clef du dico il doit chercher
};

/**
 * Optimise une chaine de caractère pour la recherche de menu
 * Mise en minuscule et remplacement des accents courant
 *
 * @param {string} string la chaine de caractère à changer
 *
 * @return {string} la chaine de caractère modifiée
 */
 function replaceForSearch(string) {
   string = string.toLowerCase();

   string = string.replace(new RegExp(/[àáâãäå]/g),"a");
   string = string.replace(new RegExp(/æ/g),"ae");
   string = string.replace(new RegExp(/ç/g),"c");
   string = string.replace(new RegExp(/[èéêë]/g),"e");
   string = string.replace(new RegExp(/[ìíîï]/g),"i");
   string = string.replace(new RegExp(/ñ/g),"n");
   string = string.replace(new RegExp(/[òóôõö]/g),"o");
   string = string.replace(new RegExp(/½/g),"oe");
   string = string.replace(new RegExp(/[ùúûü]/g),"u");
   string = string.replace(new RegExp(/[ýÿ]/g),"y");

   return string
}

function searchVentilation(search) {
   // On enlève les anciens traitements avec la classe active et le changement de classe margin
   $('.section.active').removeClass("active");
   $('.collapsible-header.active').removeClass("active");
   $('.section .no-margin').removeClass('no-margin').addClass('margin-medium');

   // on enlève les accents
   var searchSansAccent = replaceForSearch(search)

   if (search !== '') {
      // on cache toutes les sections et les search-contents
      $(".section").hide();
      $(".module-title").hide();
      $(".section .search-content").hide();

      //on passe l'icone en mode déplié
      $("#expand-all-section").html('<i class="mdi mdi-collapse-all medium left no-margin" title="Replié" ></i>');

      // On cherche l'input dans le tableau des menus
      var results = fuzzysort.go(searchSansAccent, ventilations, searchOptions);

      if (results) {
      results.forEach(function (resultItem) {
      // Récupération du label, du search-content, de son parent et de la section
      var prefLabel = resultItem['obj']['item'];
      var inputFieldPref = $(prefLabel).closest(".search-content");
      var section = $(prefLabel).closest(".section");
      var section_module = $(prefLabel).closest(".module-title");
      var parentInputField = $(inputFieldPref).closest('.row');


      // On déplie les sections concernés
      section.addClass('active');
      section.children("div").addClass("active");
      parentInputField.removeClass('no-margin').addClass('margin-medium');
      section.children('.collapsible-body').attr("style", "display : block;")
      section.show();
      section_module.show();
      inputFieldPref.show();
      });
      }
   } else {
      // Si recherche vide, on réaffiche toutes les préférences
      $('.section').children('div').removeClass("active");
      $(".section .search-content").show();
      $(".section .module-title").show();
      $(".section").show();
      $(".module_title").show();
      $('.section').children('.collapsible-body').attr("style", "display : none;");
   
      // Et on réinitialise le bouton "Déplier tout"
      $("#expand-all-section").html('<i class="mdi mdi-expand-all medium left no-margin" title="Déplier toutes les préférences"></i>');
   }
}

$('#expand-all-section').on("click", function () {
   var plie;
   // Si les sections sont toutes dépliées
   if ($(".section.active").length > 0) {
      plie = false;
      $("#expand-all-section").html('<i class="mdi mdi-expand-all medium left no-margin tooltip" title="Déplier tous les modules"></i>');
   } else {
      plie = true;
      $("#expand-all-section").html('<i class="mdi mdi-collapse-all medium left no-margin tooltip" title="Replier tous les modules"></i>');
   };

   // pour chaque section, on déplie ou replie
   for (i = 0; i < $(".section").length; i++) {
      if (plie) {
         $(".modules.collapsible").collapsible('open', i);
      } else {
         $(".modules.collapsible").collapsible('close', i);
      }
   };
});

   // Clear search profil
   $('#clear-search-profil').on('click', function () {
      $('#ventilations-search-field').val("");
      searchVentilation('');
   });

   // Création d'un tableau avec toutes les ventilations
   $(".label-search").each(function () {
      ventilations.push({
            "label": replaceForSearch($(this).text()),
            "item": $(this)
      });
   });

   // Recherche dans les ventilations/modules
   $('#ventilations-search-field').on('input', function () {
      searchVentilation($(this).val());
   });



$(document).ready(function(){
   // Création d'un tableau avec toutes les ventilations
   $(".label-search").each(function () {
      ventilations.push({
         "label": replaceForSearch($(this).text()),
         "item": $(this)
      });
   });

    // Settings View
    $('#params-table').DataTable({
        language: {
            processing:     "Traitement en cours...",
            search:         "Rechercher&nbsp;:",
            lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
            info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
            infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
            infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
            infoPostFix:    "",
            loadingRecords: "Chargement en cours...",
            zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
            emptyTable:     "Aucune donnÃ©e disponible dans le tableau",
            paginate: {
                first:      "Premier",
                previous:   "Pr&eacute;c&eacute;dent",
                next:       "Suivant",
                last:       "Dernier"
            },
            aria: {
                sortAscending:  ": activer pour trier la colonne par ordre croissant",
                sortDescending: ": activer pour trier la colonne par ordre dÃ©croissant"
            }
        }
    });

});
