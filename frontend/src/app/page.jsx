"use client"
import Top from '@/components/top'
import Vacancy from '@/components/vacancy'
import {useState, useEffect} from 'react'
import {get} from '@/requests'

export default function() {
  const [vacancies, setVacancies] = useState([])
  useEffect(() => {
    (async () => {
      setVacancies(await get('/vacancies'))
    })()
  }, [])
  console.log(vacancies)
  
  return (
    <main>
      <Top><h1>Вакансии</h1></Top>
      <div className="container">
        <div className="vacancies py-8 flex flex-col gap-3">
          {vacancies.map(v => 
            <Vacancy vacancy={v} key={v.slug}/>
          )}
          {vacancies.length == 0
            && 'Загрузка...'}
        </div>
      </div>
    </main>
  );
}
