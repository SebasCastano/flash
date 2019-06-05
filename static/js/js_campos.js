


    $("#id_b2_otro").change(
            function () {
                if(this.checked){
                    $("#id_b2_otro_especificado").prop('disabled', false)
                }else{
                    $("#id_b2_otro_especificado").prop('disabled', true)
                }
            }
        )
        $("#id_a12_consume_tipo_sustancia").change(
            function () {
                var select = $("#id_a12_consume_tipo_sustancia").val()
                if(select == "1"){
                    $("#id_a12a_tipo_sustancia").prop('disabled', false)
                }else{
                    $("#id_a12a_tipo_sustancia").prop('disabled', true)
                    $("#id_a12b_otro_tipo_sustancia").prop('disabled', true)
                }
            }
        )

        $("#id_a12a_tipo_sustancia").change(
            function () {
                var select = $("#id_a12a_tipo_sustancia").val()
                if(select == "4"){
                    $("#id_a12b_otro_tipo_sustancia").prop('disabled', false)
                }else{
                    $("#id_a12b_otro_tipo_sustancia").prop('disabled', true)
                }
            }
        )

        $("#id_b6_regimen_salud").change(
            function () {
                var select = $("#id_b6_regimen_salud").val()
                if(select == "4"){
                    $("#id_b6_otro_especificado").prop('disabled', false)
                }else{
                    $("#id_b6_otro_especificado").prop('disabled', true)
                }
            }
        )

        $("#id_a8_discapacidad").change(
            function () {
                var select = $("#id_a8_discapacidad").val()
                if(select == "1"){
                    $("#id_a8a_tipo_discapacidad").prop('disabled', false)
                }else{
                    $("#id_a8a_tipo_discapacidad").prop('disabled', true)
                }
            }
        )

        $("#id_medicion").change(
            function () {
                var select = $("#id_medicion").val()
                if(select == "2" || select == "3"){
                    $("#seccionK").hide()
                    $("#opiniones").show()
                }else{
                    $("#seccionK").show()
                    $("#opiniones").hide()
                }
            }
        )