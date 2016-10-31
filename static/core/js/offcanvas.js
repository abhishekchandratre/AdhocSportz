$(document).ready(function () {
  $('[data-toggle="offcanvas"]').click(function () {
    $('.row-offcanvas').toggleClass('active')
  });
});

$(document).ready(function () {
    //Initialize tooltips
    $('.nav-tabs > li a[title]').tooltip();
    
    //Wizard
    $('a[data-toggle="tab"]').on('show.bs.tab', function (e) {

        var $target = $(e.target);
    
        if ($target.parent().hasClass('disabled')) {
            return false;
        }
    });

    $(".next-step").click(function (e) {

        var $active = $('.wizard .nav-tabs li.active');
        $active.next().removeClass('disabled');
        nextTab($active);

    });
    $(".prev-step").click(function (e) {

        var $active = $('.wizard .nav-tabs li.active');
        prevTab($active);

    });
});

function nextTab(elem) {
    $(elem).next().find('a[data-toggle="tab"]').click();
}
function prevTab(elem) {
    $(elem).prev().find('a[data-toggle="tab"]').click();
}

$(document).ready(function() {
    var panels = $('.user-infos');
    var panelsButton = $('.dropdown-user');
    panels.hide();

    //Click dropdown
    panelsButton.click(function() {
        //get data-for attribute
        var dataFor = $(this).attr('data-for');
        var idFor = $(dataFor);

        //current button
        var currentButton = $(this);
        idFor.slideToggle(400, function() {
            //Completed slidetoggle
            if(idFor.is(':visible'))
            {
                currentButton.html('<i class="glyphicon glyphicon-chevron-up text-muted"></i>');
            }
            else
            {
                currentButton.html('<i class="glyphicon glyphicon-chevron-down text-muted"></i>');
            }
        })
    });


    $('[data-toggle="tooltip"]').tooltip();

    $('button').click(function(e) {
        e.preventDefault();
    });
});

$(document).on('submit','#user_details',function(e){
	e.preventDefault();
    var form = $(user_details);
	$.ajax({
		type: 'POST',
		url: 'core/register/basic',
		data:
            form.serialize(),
		success:function(){
			alert("created1")
		}

	});
});

$(document).on('submit','#basic_info',function(e){
	e.preventDefault();

	$.ajax({
		type: 'POST',
		url: '/register/userInfo$/',
		data:{
			id_gender:$('#id_gender').val(),
            id_birthDate:$('#id_birthDate').val(),
            id_phoneNumber:$('#id_phoneNumber').val(),
            id_oneLinerStatus:$('#id_oneLinerStatus').val(),
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
		},
		success:function(){
			alert("created2")
		}

	});
});

$(document).on('submit','#sports_interest',function(e){
	e.preventDefault();

	$.ajax({
		type: 'POST',
		url: '/register/sportsInterest$/',
		data:{
			firstName:$('#firstName').val(),
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
		},
		success:function(){
			alert("created3")
		}

	});
});