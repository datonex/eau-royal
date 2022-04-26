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
  stripe
    .confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
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
        card.update({ disabled: false });
        $('#submit-button').attr('disabled', false);
      } else {
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    });
});
