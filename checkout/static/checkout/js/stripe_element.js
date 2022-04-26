/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js

    rest of logic from Code Institute's E commerce lesson
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
  base: {
    color: '#1b112d',
    fontFamily: '"Lato", sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4',
    },
  },
  invalid: {
    color: '#dc3545',
    iconColor: '#dc3545',
  },
};
var card = elements.create('card', { style: style });
card.mount('#card-element');

// Realtime card validation handler
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
    var html = `
          <span class="icon" role="alert">
              <i class="fas fa-times fs-6"></i>
          </span>
          <span>${event.error.message}</span>
      `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = '';
  }
});

// Form submission handler
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (event) {
  event.preventDefault();
  card.update({ disabled: true });
  $('#submit-button').attr('disabled', true);
  $('#payment-form').fadeToggle(100);
  $('#loading-overlay').fadeToggle(100);

  var saveInfo = Boolean($('#id-save-info').attr('checked'));
  // From using {% csrf_token %} in the form
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    csrfmiddlewaretoken: csrfToken,
    client_secret: clientSecret,
    save_info: saveInfo,
  };
  var url = '/checkout/cache_checkout_data/';

  $.post(url, postData)
    .done(function () {
      stripe
        .confirmCardPayment(clientSecret, {
          payment_method: {
            card: card,
            billing_details: {
              name: $.trim(form.first_name.value).concat(' ', $.trim(form.last_name.value)),
              phone: $.trim(form.phone_number.value),
              email: $.trim(form.email.value),
              address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                state: $.trim(form.county.value),
                country: $.trim(form.country.value),
              },
            },
          },
          shipping: {
            name: $.trim(form.first_name.value).concat(' ', $.trim(form.last_name.value)),
            phone: $.trim(form.phone_number.value),
            address: {
              line1: $.trim(form.street_address1.value),
              line2: $.trim(form.street_address2.value),
              city: $.trim(form.town_or_city.value),
              state: $.trim(form.county.value),
              postal_code: $.trim(form.postcode.value),
              country: $.trim(form.country.value),
            },
          },
        })
        .then(function (result) {
          if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                  <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                  </span>
                  <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({ disabled: false });
            $('#submit-button').attr('disabled', false);
          } else {
            if (result.paymentIntent.status === 'succeeded') {
              form.submit();
            }
          }
        });
    })
    .fail(function () {
      // just reload the page, the error will be in django messages
      location.reload();
    });
});
