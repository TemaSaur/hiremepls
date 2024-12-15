'use client'
import { useParams } from "next/navigation"
import { useState, useEffect } from "react"
import { get } from "@/requests"
import Top from "@/components/top"
import VacancyInner from "@/components/vacancy_inner"
import Button from "@/components/button"

export default function() {
    const params = useParams()

    const [vacancy, setVacancy] = useState(null)
    const [info, setInfo] = useState(true)

    useEffect(() => {
        (async () => {
           setVacancy(await get(`/vacancies/${params.slug}`))
        })()
    }, [])
    console.log(vacancy)

    return <main>
        <Top>
            {vacancy == null
                ? 'Загрузка...'
                : <VacancyInner vacancy={vacancy} />}
            
            <div className="buttons mt-4 gap-8 flex">
                <Button active={!info}>Описание</Button>
                <Button active={info}>Отклик</Button>
            </div>
        </Top>

        <div className="container">
            {vacancy && info &&
                <div className="description py-6">
                    {vacancy.description}
                </div> }
        </div>
    </main>
}