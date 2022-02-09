function on_submit() {

    let data=document.getElementById('subinput')
    
    let res=fetch(`https://subjectapi-lioncat2002.vercel.app/subjects/${data.value}`)
    
    res
    .then(
        r=>
        r.json()
        )
    .then(
        d=>
        document.getElementById('result').innerText=`You should take: ${d.sub}`
    )
    
}
