import Vue from 'vue';
import $ from 'jquery';
import Materialize from 'materialize-css'
import template from '../../tmp/components/rating.html';

const Rate = Vue.extend({
    template,
    props: ['isLogin', 'type', 'unique'],
    data(){
        return {
            rate: [
                { mark: 1, name: "star_border" },
                { mark: 2, name: "star_border" },
                { mark: 3, name: "star_border" },
                { mark: 4, name: "star_border" },
                { mark: 5, name: "star_border" },
                { mark: 6, name: "star_border" },
                { mark: 7, name: "star_border" },
                { mark: 8, name: "star_border" },
                { mark: 9, name: "star_border" },
                { mark: 10, name: "star_border" },
            ],
            allRate: 0,
            session: '',
            activated: false,
            showCommonRate: false
        }
    },
    created(){
        this.getRate()
    },
    methods: {
        getRate(){
            let self = this,
                uri = `/api/1/rating/${self.unique}/${self.type}/`;
            $.get(uri).done(data => {
                if (data.value === null){
                    self.allRate = 0 
                } else {
                    self.allRate = data.value;
                    self.allRate = self.allRate.toFixed(1)
                    self.colorStars(data.value)
                }
               
            })
        },
        colorStars(mark){
            this.rate.forEach((item, i) => {
                if (mark > i) {
                    item.name = "star"
                } else {
                    item.name = "star_border"
                }
            })
        },
        unsetStars(){
            if (this.activated = false) {
                this.rate.forEach((item) => {
                    item.name = "star_border"
                })
            }
        },
        getSess(){
           return document.getElementById('session_id').innerHTML;
        },  
        setStars(mark){
            let self = this,
                uri = '/api/1/vote/',
                params = {
                    sessionid: self.getSess(),
                    app: self.type,
                    key: self.unique,
                    vote: mark
                };

            self.activated = true
            self.colorStars(mark)

            $.post(uri, params).done(data => {
                if (data.value){
                    self.colorStars(data.value);
                    self.successAction("Оценка учтена!");
                    self.getRate()
                }
            }).fail(error => {
                console.log(error)
            })
        },
        successAction(message){
            Materialize.toast(message, 4000)
        }
    }

})

export default Rate;
