(function ($) {
    $(function () {
        $('.contacts-plugin input[type=submit]').on('click', function (event) {
            var $form = $(this).parents('form').eq(0);

            function handleResponse(data) {
                //    TODO: Write the body of this function
                if (data.pk) {
                    $form.siblings('.success').html(data.success).show(100);
                    $form.add('.legend').hide(100);
                } else {
                    $form.find('.errors').empty();
                    $.each2(data, (key, value) => {
                        var $field = $form.find('input[name=' + key + ']').first();
                        $field.parents('.field-wrapper').find('.errors').html(value.join(' '));
                    });
                    if (data.__all__) {
                        $form.siblings('.errors').find('.form-errors').html(data.__all__.join(' '))
                    } else {
                        $form.siblings('.errors').find('.form-errors').empty()
                    }
                    $form.siblings('.errors').show(100);
                }
            }

            event.preventDefault();
            $form.siblings('.errors, .success').hide(100);
            $.ajax({
                type: 'POST',
                url: $form.attr('action'),
                data: $form.serialize()
            }).always(handleResponse())
        })
    })
}(window.jQuery));