import Top from "@/components/top"
import AuthForm from "@/components/auth_form"

export default function Login() {
    return <main>
        <Top><h1>Регистрация</h1></Top>

        <div className="flex flex-col items-center py-8">
            <AuthForm type={'register'} />

            <a className="mt-4" href="/login">Уже есть аккаунт? Войти</a>
        </div>
    </main>
}