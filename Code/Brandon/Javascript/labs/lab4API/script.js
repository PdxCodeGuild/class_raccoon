// Vue App ---
let app = new Vue({
    el:'#app',
    data: {
        drinkName:'',
        drinkResults:'',

    },
    methods: {
        startFind: function(){
            axios({
                method: 'get',
                url: 'https://api.funtranslations.com/translate/yoda.json?',
                params: {
                    text: this.drinkName,


                }

            })
            .then((response) => {
                this.drinkResults = response.data.contents
                console.log(this.drinkResults)
            })
        }
    }

})