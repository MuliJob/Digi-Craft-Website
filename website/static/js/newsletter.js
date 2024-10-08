$(document).ready(function() {
  function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

  const csrftoken = getCookie('csrftoken');

  $(document).on('submit', '#newsletter-subscription', function(event) {
      event.preventDefault();
      
      const form = $(this);
      const submitButton = $('#submit-button');

      submitButton.html('<i class="fas fa-spinner fa-spin"></i> Subscribing...');
      submitButton.prop('disabled', true);

      $.ajax({
          url: '/newsletter/subscribe/',
          type: 'POST',
          data: form.serialize(),
          headers: { 'X-CSRFToken': csrftoken },
          dataType: 'json',
          success: function(data) {
              if (data.success) {
                  toastr.success(data.success, 'Subscribed Successfully!');
              } else if (data.error) {
                  toastr.warning(data.error, 'Warning');
              }
              form.trigger('reset');
          },
          error: function(xhr, errmsg, err) {
              toastr.error('There was an issue with your subscription.', 'Error');
          },
          complete: function() {
              submitButton.html('Subscribe');
              submitButton.prop('disabled', false);
          }
      });
  });
});

toastr.options = {
  "closeButton": true,
  "debug": false,
  "newestOnTop": false,
  "progressBar": true,
  "positionClass": "toast-bottom-right",
  "preventDuplicates": true,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "5000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
};
