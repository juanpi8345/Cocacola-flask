jQuery(document).ready(listo); /* Una vez que nuestra web esta lista vamos a hacer cosas con los elementos*/

function listo(){

   jQuery(".hamb").click(function(e){
        e.preventDefault();

   jQuery("header .container nav").toggleClass("open");
   jQuery(".hamb i").toggleClass("fa-times");

   });

   jQuery("header .container nav a").click(function(){

   
    jQuery("header .container nav").removeClass("open");
    jQuery(".hamb i").removeClass("fa-times");
   	var dev = jQuery(this).attr("href"); /* Atributo Href */

   	jQuery("html,body").animate({
   		"scrollTop": jQuery(dev).offset().top -76
   	})
   })

   jQuery("#inicio .bloque-inicio .boton-rojo").click(function(){

   	var dev = jQuery(this).attr("href")

   	jQuery("html,body").animate({
   		"scrollTop": jQuery(dev).offset().top -76
   	})
   })

}


/* Cuando la web esta lista se ejecutara la funcion */
