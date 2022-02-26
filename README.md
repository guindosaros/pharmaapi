[![Build Status](https://app.travis-ci.com/guindosaros/pharmaapi.svg?branch=master)](https://app.travis-ci.com/guindosaros/pharmaapi)

### structuture vuejs avec validation de donnees
<script>
    Vue.use(window.vuelidate.default)
    const { required, minLength, email, sameAs, maxStartDate } = window.validators;
    var app = new Vue({
        el: '#detail',
        data: {
            base_url: window.location.protocol + "//" + window.location.host + "/",
            
            

        },
        validations: {
            
        },
        delimiters: ["${", "}"],
        mounted() {
           

        },
        methods: {
            status(validation) {
                return {
                    error: validation.$error,
                    dirty: validation.$dirty
                }
            },

            

            

            
        },
    })
</script>