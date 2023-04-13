class Data{

    constructor(data){
        this.data = data
        console.log(data)
    }

    change_date(){
        let item_0 = this.data[0]

        if( item_0['create_date'] != undefined) {
            for (var i = 0 ; i < this.data.length-1; i ++){
                this.data[i]['create_date'] = this.data[i]['create_date'].substring(0,10)
            }
        }
    }

    get_data(){
        return this.data
    }

}

export {
    Data
}