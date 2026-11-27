import streamlit as st
from datetime import datetime

# ==========================================
# 1. НАСТРОЙКИ
# ==========================================

st.set_page_config(
    page_title="Construct AI",
    page_icon="🏗️",
    layout="wide"
)

# ==========================================
# 2. ДАННЫЕ
# ==========================================

if "reports" not in st.session_state:
    st.session_state.reports = []

if "page" not in st.session_state:
    st.session_state.page = "Главная"

# ==========================================
# 3. ДИЗАЙН
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: Inter, sans-serif;
}

.stApp {
    background-color: #F3F6FA;
}

[data-testid="stSidebar"] {
    background-color: #142B43;
}

[data-testid="stSidebar"] * {
    color: white;
}

.hero {
    background: linear-gradient(120deg, #173650, #28618A);
    padding: 42px;
    border-radius: 18px;
    color: white;
    margin-bottom: 30px;
}

.hero h1 {
    color: white;
    font-size: 42px;
    font-weight: 800;
}

.hero p {
    color: #E0EAF3;
    font-size: 16px;
}

.card {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 24px;
    min-height: 175px;
}

.card h3 {
    color: #18354F;
    font-size: 19px;
}

.card p {
    color: #64748B;
    font-size: 14px;
}

.stButton > button {
    background: #245C83;
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 600;
    min-height: 42px;
}

.stButton > button:hover {
    background: #173D5C;
    color: white;
}

h1, h2, h3 {
    color: #18354F;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. БОКОВОЕ МЕНЮ
# ==========================================

with st.sidebar:

    st.markdown("## 🏗️ Construct AI")

    st.caption("Эксперт по строительным нормам Казахстана")

    st.divider()

    st.markdown("### ГЛАВНОЕ МЕНЮ")

    page = st.radio(
        "Разделы",
        [
            "Главная",
            "Проверка проекта",
            "Поиск нормативов",
            "Мои отчёты"
        ],
        key="page",
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("**Construct AI**")
    st.caption("Интеллектуальная платформа для архитектуры и строительства")
    st.caption("Казахстан 🇰🇿")

# ==========================================
# 5. ГЛАВНАЯ СТРАНИЦА
# ==========================================

if page == "Главная":

    st.markdown("""
    <div class="hero">
        <h1>Construct AI</h1>
        <p>
        Интеллектуальная платформа для анализа
        архитектурных и строительных проектов
        по нормативам Республики Казахстан.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.header("Возможности платформы")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📐 Проверка проекта</h3>
            <p>
            Ввод параметров здания и предварительный
            анализ архитектурного проекта.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>📚 Строительные нормы</h3>
            <p>
            Поиск требований и работа
            с нормативными документами Казахстана.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>📄 Отчёты</h3>
            <p>
            Сохранение результатов обработки
            и формирование отчётов.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.header("Начать работу")

    if st.button(
        "Перейти к проверке проекта →",
        use_container_width=True
    ):
        st.session_state.page = "Проверка проекта"
        st.rerun()

    st.info(
        "Платформа находится в стадии разработки. "
        "Автоматическая проверка нормативов будет "
        "подключена на следующем этапе."
    )

# ==========================================
# 6. ПРОВЕРКА ПРОЕКТА
# ==========================================

elif page == "Проверка проекта":

    st.title("📐 Проверка архитектурного проекта")

    st.write(
        "Введите основные характеристики здания "
        "для предварительного анализа."
    )

    st.divider()

    with st.form("project_form"):

        st.subheader("Основные параметры здания")

        building_type = st.selectbox(
            "Тип здания",
            [
                "Жилое здание",
                "Общественное здание",
                "Административное здание",
                "Образовательное учреждение",
                "Торговый центр",
                "Производственное здание"
            ]
        )

        col1, col2 = st.columns(2)

        with col1:
            floors = st.number_input(
                "Количество этажей",
                min_value=1,
                max_value=100,
                value=5
            )

            height = st.number_input(
                "Высота здания (м)",
                min_value=1.0,
                max_value=500.0,
                value=15.0,
                step=0.5
            )

        with col2:
            area = st.number_input(
                "Общая площадь (м²)",
                min_value=1.0,
                max_value=1000000.0,
                value=1000.0,
                step=10.0
            )

            location = st.text_input(
                "Местоположение объекта",
                placeholder="Например: Алматы"
            )

        submitted = st.form_submit_button(
            "Начать анализ проекта",
            use_container_width=True
        )

    if submitted:

        report = {
            "date": datetime.now().strftime("%d.%m.%Y %H:%M"),
            "building_type": building_type,
            "floors": int(floors),
            "height": float(height),
            "area": float(area),
            "location": location.strip() or "Не указано"
        }

        st.session_state.reports.insert(0, report)

        st.success("Данные проекта успешно приняты!")

        st.subheader("Результаты обработки")

        c1, c2, c3 = st.columns(3)

        c1.metric("Количество этажей", floors)
        c2.metric("Высота здания", f"{height} м")
        c3.metric("Общая площадь", f"{area:,.0f} м²")

        st.write("**Тип здания:**", building_type)
        st.write("**Местоположение:**", report["location"])

        st.warning(
            "Это предварительная обработка введённых данных. "
            "Соответствие строительным нормам пока не проверено."
        )

        st.info("Данные сохранены в разделе «Мои отчёты».")

# ==========================================
# 7. ПОИСК НОРМАТИВОВ
# ==========================================

elif page == "Поиск нормативов":

    st.title("📚 Поиск строительных нормативов")

    st.write(
        "Раздел предназначен для поиска требований "
        "в нормативных документах Республики Казахстан."
    )

    st.divider()

    query = st.text_input(
        "Введите поисковый запрос",
        placeholder="Например: требования к эвакуационным выходам"
    )

    category = st.selectbox(
        "Категория нормативов",
        [
            "Все категории",
            "Жилые здания",
            "Общественные здания",
            "Пожарная безопасность",
            "Конструктивные решения",
            "Доступность и безопасность"
        ]
    )

    if st.button("Найти нормативы"):

        if query.strip():

            st.info(f"Запрос: {query}")
            st.write(f"Категория: {category}")

            st.warning(
                "Нормативная база ещё не подключена. "
                "Реальный поиск документов будет реализован "
                "на следующем этапе."
            )

        else:
            st.error("Введите поисковый запрос.")

    st.divider()

    st.subheader("Нормативная база Казахстана")

    st.write(
        "Здесь будет размещена база официальных "
        "строительных нормативов с поиском по документам "
        "и отдельным пунктам."
    )

# ==========================================
# 8. МОИ ОТЧЁТЫ
# ==========================================

elif page == "Мои отчёты":

    st.title("📄 Мои отчёты")

    st.write("История обработки архитектурных проектов.")

    st.divider()

    if not st.session_state.reports:

        st.info(
            "Отчётов пока нет. Создайте первый отчёт "
            "в разделе «Проверка проекта»."
        )

    else:

        st.metric(
            "Количество отчётов",
            len(st.session_state.reports)
        )

        for index, report in enumerate(
            st.session_state.reports
        ):

            with st.expander(
                f"Отчёт №{index + 1} — {report['date']}"
            ):

                st.write("**Тип здания:**", report["building_type"])
                st.write("**Этажность:**", report["floors"])
                st.write("**Высота:**", report["height"], "м")
                st.write("**Площадь:**", report["area"], "м²")
                st.write("**Местоположение:**", report["location"])

                report_text = f"""
CONSTRUCT AI
ОТЧЁТ О ПРОЕКТЕ

Номер отчёта: {index + 1}
Дата: {report['date']}

Тип здания: {report['building_type']}
Количество этажей: {report['floors']}
Высота: {report['height']} м
Общая площадь: {report['area']} м²
Местоположение: {report['location']}

Статус: предварительная обработка данных.
Нормативная экспертиза не проводилась.
"""

                st.download_button(
                    "⬇️ Скачать отчёт",
                    data=report_text,
                    file_name=f"construct_ai_report_{index + 1}.txt",
                    mime="text/plain",
                    key=f"download_{index}"
                )

# ==========================================
# 9. ПОДВАЛ САЙТА
# ==========================================

st.divider()

st.caption(
    "© 2026 Construct AI | "
    "Интеллектуальные решения для архитектуры и строительства"
)